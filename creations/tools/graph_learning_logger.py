```python
#!/usr/bin/env python3
"""
GraphLog: A comprehensive logging utility for graph generation and tracking

Supports:
- Detailed error logging
- Performance tracking
- Configurable output destinations
- Exception handling for graph-related processes

Example Usage:
    logger = GraphLogger(log_file='graph_generation.log')
    
    with logger.process('Creating network graph'):
        try:
            graph = generate_complex_graph()
            logger.success(f'Generated graph with {len(graph.nodes)} nodes')
        except GraphGenerationError as e:
            logger.error(f'Graph generation failed: {e}')
"""

import os
import sys
import time
import logging
from contextlib import contextmanager
from typing import Optional, Any, Dict, Callable

class GraphLogger:
    def __init__(
        self, 
        log_file: Optional[str] = None, 
        log_level: int = logging.INFO,
        console_output: bool = True
    ):
        """
        Initialize comprehensive graph logging system.
        
        Args:
            log_file: Path to log file. Creates if not exists.
            log_level: Logging verbosity threshold
            console_output: Enable stdout logging
        """
        self.logger = logging.getLogger('GraphLogger')
        self.logger.setLevel(log_level)
        
        # Formatters
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)8s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_formatter = logging.Formatter(
            '%(levelname)8s: %(message)s'
        )
        
        # File Handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
        
        # Console Handler
        if console_output:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(console_formatter)
            self.logger.addHandler(console_handler)
    
    @contextmanager
    def process(self, description: str):
        """
        Context manager for tracking process duration and status.
        
        Args:
            description: Brief description of the process
        """
        start_time = time.time()
        self.logger.info(f"START: {description}")
        
        try:
            yield
            duration = time.time() - start_time
            self.logger.info(f"COMPLETED: {description} (Duration: {duration:.2f}s)")
        
        except Exception as e:
            duration = time.time() - start_time
            self.logger.error(f"FAILED: {description} (Duration: {duration:.2f}s)")
            self.logger.error(f"Error Details: {str(e)}")
            raise
    
    def success(self, message: str):
        """Log successful operation."""
        self.logger.info(f"✓ {message}")
    
    def error(self, message: str):
        """Log error with standard formatting."""
        self.logger.error(f"✗ {message}")
    
    def metric(self, name: str, value: Any):
        """
        Log performance or statistical metrics.
        
        Args:
            name: Metric identifier
            value: Metric value
        """
        self.logger.info(f"METRIC: {name} = {value}")

def main():
    """Demonstration of GraphLogger capabilities."""
    logger = GraphLogger(log_file='demo_graph.log')
    
    with logger.process('Simulating graph generation'):
        try:
            # Simulated graph generation
            nodes = 1000
            edges = 5000
            
            logger.metric('Total Nodes', nodes)
            logger.metric('Total Edges', edges)
            
            if nodes > 500:
                logger.success(f'Large graph generated: {nodes} nodes')
            
        except Exception as e:
            logger.error(f'Graph generation simulation failed: {e}')

if __name__ == '__main__':
    main()
```