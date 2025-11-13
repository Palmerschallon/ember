#!/usr/bin/env python3
"""
Ember Performance Monitoring & Alerting System
"""
import asyncio
import time
import psutil
import aiohttp
import json
import os
from datetime import datetime, timedelta
from collections import deque
from typing import Dict, List, Tuple
import logging
from dataclasses import dataclass, asdict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Metric:
    name: str
    value: float
    timestamp: float
    tags: Dict[str, str] = None

class MetricsCollector:
    def __init__(self, window_size: int = 300):  # 5 minute window
        self.metrics: Dict[str, deque] = {}
        self.window_size = window_size
        self.alerts = []
        
    def record(self, name: str, value: float, tags: Dict[str, str] = None):
        """Record a metric value"""
        if name not in self.metrics:
            self.metrics[name] = deque()
        
        metric = Metric(name, value, time.time(), tags)
        self.metrics[name].append(metric)
        
        # Clean old metrics
        cutoff = time.time() - self.window_size
        while self.metrics[name] and self.metrics[name][0].timestamp < cutoff:
            self.metrics[name].popleft()
    
    def get_stats(self, name: str) -> Dict[str, float]:
        """Get statistics for a metric"""
        if name not in self.metrics or not self.metrics[name]:
            return {}
        
        values = [m.value for m in self.metrics[name]]
        return {
            "count": len(values),
            "mean": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
            "latest": values[-1]
        }

class EmberMonitor:
    def __init__(self, health_url: str = "http://localhost:8080/health", 
                 ws_url: str = "ws://localhost:8083"):
        self.health_url = health_url
        self.ws_url = ws_url
        self.collector = MetricsCollector()
        self.process = None
        self.alerts_enabled = True
        
        # Alert thresholds
        self.thresholds = {
            "cpu_percent": 80.0,
            "memory_percent": 85.0,
            "response_time_ms": 5000,
            "error_rate": 0.1,  # 10%
            "ws_connections": 100,
            "queue_size": 500
        }
    
    async def collect_system_metrics(self):
        """Collect system resource metrics"""
        try:
            # Find Ember process
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                if 'websocket_server.py' in str(proc.info.get('cmdline', [])):
                    self.process = proc
                    break
            
            if self.process:
                # CPU and Memory
                cpu = self.process.cpu_percent(interval=0.1)
                memory = self.process.memory_percent()
                
                self.collector.record("cpu_percent", cpu)
                self.collector.record("memory_percent", memory)
                
                # Connection count
                connections = len(self.process.connections())
                self.collector.record("connections", connections)
                
                logger.info(f"📊 System: CPU={cpu:.1f}%, Memory={memory:.1f}%, Connections={connections}")
                
        except (psutil.NoSuchProcess, AttributeError):
            self.process = None
            logger.warning("⚠️  Ember process not found")
    
    async def check_health_endpoint(self):
        """Check HTTP health endpoint"""
        start_time = time.time()
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.health_url, timeout=5) as response:
                    response_time = (time.time() - start_time) * 1000  # ms
                    self.collector.record("response_time_ms", response_time)
                    
                    if response.status == 200:
                        self.collector.record("health_check_success", 1)
                        data = await response.json()
                        
                        # Extract metrics from health response
                        if 'connections' in data:
                            self.collector.record("ws_connections", data['connections'])
                        if 'queue_size' in data:
                            self.collector.record("queue_size", data['queue_size'])
                            
                        logger.info(f"✅ Health check OK: {response_time:.0f}ms")
                    else:
                        self.collector.record("health_check_success", 0)
                        logger.error(f"❌ Health check failed: {response.status}")
                        
        except Exception as e:
            self.collector.record("health_check_success", 0)
            logger.error(f"❌ Health check error: {e}")
    
    async def check_alerts(self):
        """Check metrics against thresholds and generate alerts"""
        if not self.alerts_enabled:
            return
        
        alerts = []
        
        for metric_name, threshold in self.thresholds.items():
            stats = self.collector.get_stats(metric_name)
            if stats and 'latest' in stats:
                value = stats['latest']
                
                if value > threshold:
                    alert = {
                        "severity": "warning" if value < threshold * 1.2 else "critical",
                        "metric": metric_name,
                        "value": value,
                        "threshold": threshold,
                        "message": f"{metric_name} is {value:.1f} (threshold: {threshold})",
                        "timestamp": datetime.now().isoformat()
                    }
                    alerts.append(alert)
        
        # Check error rate
        success_stats = self.collector.get_stats("health_check_success")
        if success_stats and success_stats['count'] > 10:
            error_rate = 1 - (success_stats['mean'])
            if error_rate > self.thresholds['error_rate']:
                alerts.append({
                    "severity": "critical",
                    "metric": "error_rate",
                    "value": error_rate,
                    "threshold": self.thresholds['error_rate'],
                    "message": f"High error rate: {error_rate*100:.1f}%",
                    "timestamp": datetime.now().isoformat()
                })
        
        # Log alerts
        for alert in alerts:
            if alert['severity'] == 'critical':
                logger.error(f"🚨 CRITICAL: {alert['message']}")
            else:
                logger.warning(f"⚠️  WARNING: {alert['message']}")
        
        # Save alerts to file for external monitoring
        if alerts:
            with open("/media/palmerschallon/ThePod1/alerts.json", "w") as f:
                json.dump(alerts, f, indent=2)
    
    def get_dashboard_data(self) -> Dict:
        """Get data for monitoring dashboard"""
        metrics = {}
        
        for metric_name in self.collector.metrics:
            metrics[metric_name] = self.collector.get_stats(metric_name)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "metrics": metrics,
            "alerts": self.alerts_enabled,
            "thresholds": self.thresholds,
            "process_running": self.process is not None
        }
    
    async def run(self, interval: int = 10):
        """Run monitoring loop"""
        logger.info("🚀 Starting Ember Monitor")
        
        while True:
            try:
                # Collect all metrics
                await asyncio.gather(
                    self.collect_system_metrics(),
                    self.check_health_endpoint(),
                    return_exceptions=True
                )
                
                # Check for alerts
                await self.check_alerts()
                
                # Save dashboard data
                dashboard_data = self.get_dashboard_data()
                with open("/media/palmerschallon/ThePod1/monitor_dashboard.json", "w") as f:
                    json.dump(dashboard_data, f, indent=2)
                
            except Exception as e:
                logger.error(f"❌ Monitoring error: {e}")
            
            await asyncio.sleep(interval)

# Monitoring dashboard generator
def generate_dashboard_html():
    """Generate a simple HTML dashboard"""
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Ember Monitor Dashboard</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               margin: 20px; background: #0a0a0a; color: #fff; }
        .metric { background: #1a1a1a; border-radius: 8px; padding: 15px; margin: 10px 0;
                  border: 1px solid #333; }
        .metric-value { font-size: 2em; font-weight: bold; color: #4CAF50; }
        .alert { background: #ff4444; color: white; padding: 10px; border-radius: 4px; margin: 5px 0; }
        .warning { background: #ff9800; }
        h1 { color: #ff6b6b; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; }
    </style>
    <meta http-equiv="refresh" content="5">
</head>
<body>
    <h1>🔥 Ember Monitor Dashboard</h1>
    <div id="dashboard">
        <p>Loading metrics...</p>
    </div>
    
    <script>
        fetch('/media/palmerschallon/ThePod1/monitor_dashboard.json')
            .then(r => r.json())
            .then(data => {
                let html = '<div class="stats">';
                
                for (const [name, stats] of Object.entries(data.metrics)) {
                    if (stats.latest !== undefined) {
                        html += `<div class="metric">
                            <h3>${name}</h3>
                            <div class="metric-value">${stats.latest.toFixed(1)}</div>
                            <small>Min: ${stats.min.toFixed(1)} | Max: ${stats.max.toFixed(1)}</small>
                        </div>`;
                    }
                }
                
                html += '</div>';
                document.getElementById('dashboard').innerHTML = html;
            })
            .catch(e => console.error(e));
    </script>
</body>
</html>"""
    
    with open("/media/palmerschallon/ThePod1/monitor_dashboard.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    # Generate dashboard
    generate_dashboard_html()
    
    # Run monitor
    monitor = EmberMonitor()
    asyncio.run(monitor.run())