"""
WebSocket Protocol Definition for Ember
"""
from typing import Dict, Any, Optional, Literal
from dataclasses import dataclass, asdict
import json
import time
import uuid
from enum import Enum

class MessageType(Enum):
    # Client -> Server
    CREATE_REQUEST = "create_request"
    ITERATE_REQUEST = "iterate_request"
    HEARTBEAT = "heartbeat"
    
    # Server -> Client
    CREATE_RESPONSE = "create_response"
    PROGRESS_UPDATE = "progress_update"
    ERROR = "error"
    SERVER_INFO = "server_info"
    HEARTBEAT_ACK = "heartbeat_ack"

class ErrorCode(Enum):
    RATE_LIMIT = "RATE_LIMIT"
    INVALID_REQUEST = "INVALID_REQUEST"
    API_ERROR = "API_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    TIMEOUT = "TIMEOUT"

@dataclass
class WSMessage:
    """Standard WebSocket message format"""
    id: str
    type: MessageType
    timestamp: float
    version: str = "1.0"
    data: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None
    
    @classmethod
    def create(cls, msg_type: MessageType, data: Dict[str, Any] = None) -> 'WSMessage':
        """Create a new message with auto-generated ID and timestamp"""
        return cls(
            id=str(uuid.uuid4()),
            type=msg_type,
            timestamp=time.time(),
            data=data
        )
    
    def to_json(self) -> str:
        """Serialize message to JSON"""
        msg_dict = asdict(self)
        msg_dict['type'] = self.type.value
        return json.dumps(msg_dict)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'WSMessage':
        """Deserialize message from JSON"""
        data = json.loads(json_str)
        return cls(
            id=data['id'],
            type=MessageType(data['type']),
            timestamp=data['timestamp'],
            version=data.get('version', '1.0'),
            data=data.get('data'),
            error=data.get('error')
        )

class WSProtocol:
    """WebSocket protocol handler with versioning support"""
    
    SUPPORTED_VERSIONS = ["1.0", "1.1"]
    
    @staticmethod
    def create_request(request_type: str, prompt: str, **kwargs) -> str:
        """Create a standardized creation request"""
        msg = WSMessage.create(
            MessageType.CREATE_REQUEST,
            data={
                "type": request_type,
                "prompt": prompt,
                "options": kwargs
            }
        )
        return msg.to_json()
    
    @staticmethod
    def progress_update(request_id: str, status: str, progress: float, details: str = "") -> str:
        """Create a progress update message"""
        msg = WSMessage.create(
            MessageType.PROGRESS_UPDATE,
            data={
                "request_id": request_id,
                "status": status,
                "progress": progress,
                "details": details
            }
        )
        return msg.to_json()
    
    @staticmethod
    def error_response(request_id: str, code: ErrorCode, message: str, retry_after: Optional[int] = None) -> str:
        """Create an error response"""
        msg = WSMessage.create(
            MessageType.ERROR,
            error={
                "code": code.value,
                "message": message,
                "request_id": request_id,
                "retry_after": retry_after
            }
        )
        return msg.to_json()
    
    @staticmethod
    def server_info(connections: int, version: str, capabilities: list) -> str:
        """Send server information"""
        msg = WSMessage.create(
            MessageType.SERVER_INFO,
            data={
                "active_connections": connections,
                "server_version": version,
                "protocol_version": "1.0",
                "capabilities": capabilities,
                "limits": {
                    "max_request_size": 100000,
                    "rate_limit": 10,
                    "max_connections": 100
                }
            }
        )
        return msg.to_json()

# Example client handler with protocol
class ProtocolHandler:
    def __init__(self, websocket):
        self.websocket = websocket
        self.client_version = None
        
    async def handle_message(self, raw_message: str):
        """Handle incoming message with protocol validation"""
        try:
            msg = WSMessage.from_json(raw_message)
            
            # Version check
            if msg.version not in WSProtocol.SUPPORTED_VERSIONS:
                await self.send_error(
                    msg.id,
                    ErrorCode.INVALID_REQUEST,
                    f"Unsupported protocol version: {msg.version}"
                )
                return
            
            # Route by message type
            if msg.type == MessageType.CREATE_REQUEST:
                await self.handle_create_request(msg)
            elif msg.type == MessageType.HEARTBEAT:
                await self.send_heartbeat_ack(msg.id)
            else:
                await self.send_error(
                    msg.id,
                    ErrorCode.INVALID_REQUEST,
                    f"Unknown message type: {msg.type}"
                )
                
        except json.JSONDecodeError:
            await self.websocket.send(WSProtocol.error_response(
                "unknown",
                ErrorCode.INVALID_REQUEST,
                "Invalid JSON format"
            ))
        except Exception as e:
            await self.websocket.send(WSProtocol.error_response(
                "unknown",
                ErrorCode.INTERNAL_ERROR,
                str(e)
            ))
    
    async def handle_create_request(self, msg: WSMessage):
        """Handle creation request with progress updates"""
        request_id = msg.id
        
        # Send immediate acknowledgment
        await self.websocket.send(WSProtocol.progress_update(
            request_id,
            "received",
            0.1,
            "Request received and queued"
        ))
        
        # Simulate processing with progress updates
        await self.websocket.send(WSProtocol.progress_update(
            request_id,
            "processing",
            0.5,
            "Generating with Claude API"
        ))
        
        # Process actual request
        # ... your creation logic here ...
        
        await self.websocket.send(WSProtocol.progress_update(
            request_id,
            "complete",
            1.0,
            "Creation complete"
        ))
    
    async def send_heartbeat_ack(self, msg_id: str):
        """Acknowledge heartbeat"""
        ack = WSMessage.create(
            MessageType.HEARTBEAT_ACK,
            data={"original_id": msg_id}
        )
        await self.websocket.send(ack.to_json())
    
    async def send_error(self, request_id: str, code: ErrorCode, message: str):
        """Send error message"""
        await self.websocket.send(
            WSProtocol.error_response(request_id, code, message)
        )