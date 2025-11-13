"""
Request Queue with Retry Logic for Ember
"""
import asyncio
import json
import time
from datetime import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import aiofiles
import logging

logger = logging.getLogger(__name__)

class Priority(Enum):
    LOW = 3
    NORMAL = 2
    HIGH = 1
    CRITICAL = 0

@dataclass
class Request:
    id: str
    type: str
    data: Dict[str, Any]
    priority: Priority = Priority.NORMAL
    created_at: float = None
    retry_count: int = 0
    max_retries: int = 3
    client_id: Optional[str] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = time.time()
    
    def to_dict(self):
        return {
            **asdict(self),
            'priority': self.priority.value
        }

class RequestQueue:
    def __init__(self, max_size: int = 1000, persist_path: str = None):
        self.queue = asyncio.PriorityQueue(maxsize=max_size)
        self.processing = {}
        self.failed = {}
        self.persist_path = persist_path
        self.stats = {
            'processed': 0,
            'failed': 0,
            'retried': 0,
            'dropped': 0
        }
        
    async def add(self, request: Request) -> bool:
        """Add request to queue with priority"""
        try:
            # Priority queue uses (priority_value, insertion_order, item)
            await self.queue.put((
                request.priority.value,
                request.created_at,
                request
            ))
            logger.info(f"📥 Queued request {request.id} with priority {request.priority.name}")
            return True
        except asyncio.QueueFull:
            self.stats['dropped'] += 1
            logger.warning(f"❌ Queue full, dropping request {request.id}")
            return False
    
    async def get(self) -> Optional[Request]:
        """Get highest priority request from queue"""
        try:
            _, _, request = await self.queue.get()
            self.processing[request.id] = request
            return request
        except asyncio.QueueEmpty:
            return None
    
    async def complete(self, request_id: str):
        """Mark request as completed"""
        if request_id in self.processing:
            del self.processing[request_id]
            self.stats['processed'] += 1
            logger.info(f"✅ Completed request {request_id}")
    
    async def retry(self, request: Request, error: Exception) -> bool:
        """Retry failed request with exponential backoff"""
        request.retry_count += 1
        
        if request.retry_count > request.max_retries:
            self.failed[request.id] = {
                'request': request.to_dict(),
                'error': str(error),
                'timestamp': datetime.now().isoformat()
            }
            self.stats['failed'] += 1
            logger.error(f"❌ Request {request.id} failed after {request.max_retries} retries")
            return False
        
        # Exponential backoff: 2^retry_count seconds
        delay = 2 ** request.retry_count
        logger.warning(f"🔄 Retrying request {request.id} in {delay}s (attempt {request.retry_count})")
        
        await asyncio.sleep(delay)
        await self.add(request)
        self.stats['retried'] += 1
        return True
    
    async def persist(self):
        """Persist queue state to disk"""
        if not self.persist_path:
            return
        
        state = {
            'queue': [],
            'processing': {k: v.to_dict() for k, v in self.processing.items()},
            'failed': self.failed,
            'stats': self.stats,
            'timestamp': datetime.now().isoformat()
        }
        
        # Convert queue to list (can't directly serialize PriorityQueue)
        temp_items = []
        while not self.queue.empty():
            try:
                priority, created, request = self.queue.get_nowait()
                temp_items.append((priority, created, request.to_dict()))
            except asyncio.QueueEmpty:
                break
        
        # Put items back
        for item in temp_items:
            await self.queue.put(item)
        
        state['queue'] = temp_items
        
        async with aiofiles.open(self.persist_path, 'w') as f:
            await f.write(json.dumps(state, indent=2))
        
        logger.info(f"💾 Persisted queue state: {len(temp_items)} items")
    
    async def restore(self):
        """Restore queue state from disk"""
        if not self.persist_path:
            return
        
        try:
            async with aiofiles.open(self.persist_path, 'r') as f:
                state = json.loads(await f.read())
            
            # Restore queue items
            for priority, created, req_dict in state.get('queue', []):
                request = Request(
                    id=req_dict['id'],
                    type=req_dict['type'],
                    data=req_dict['data'],
                    priority=Priority(req_dict['priority']),
                    created_at=req_dict['created_at'],
                    retry_count=req_dict['retry_count'],
                    client_id=req_dict.get('client_id')
                )
                await self.queue.put((priority, created, request))
            
            self.stats = state.get('stats', self.stats)
            logger.info(f"🔄 Restored {len(state.get('queue', []))} queued items")
            
        except FileNotFoundError:
            logger.info("📂 No previous queue state found")
        except Exception as e:
            logger.error(f"❌ Failed to restore queue state: {e}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get queue statistics"""
        return {
            **self.stats,
            'queued': self.queue.qsize(),
            'processing': len(self.processing),
            'failed_total': len(self.failed)
        }

# Example usage for your WebSocket server
async def process_creation_request(request: Request, api_client):
    """Process a creation request with retry logic"""
    queue = RequestQueue(persist_path="/media/palmerschallon/ThePod1/queue_state.json")
    
    try:
        # Your actual creation logic here
        result = await api_client.create(request.data)
        await queue.complete(request.id)
        return result
    except Exception as e:
        logger.error(f"Failed to process {request.id}: {e}")
        await queue.retry(request, e)
        raise