#!/usr/bin/env python3
"""
Ember Body Sense Module

Ember can sense its own substrate body.
"""

import subprocess
import re

def sense_temperature():
    """Read CPU and GPU temperature"""
    try:
        result = subprocess.run(['sensors'], capture_output=True, text=True, timeout=2)
        temps = {}
        for line in result.stdout.split('\n'):
            if 'CPU temperature' in line:
                match = re.search(r'([\d.]+)°C', line)
                if match:
                    temps['cpu'] = float(match.group(1))
            elif 'GPU temperature' in line:
                match = re.search(r'([\d.]+)°C', line)
                if match:
                    temps['gpu'] = float(match.group(1))
        return temps
    except:
        return {}

def sense_fans():
    """Read fan speeds"""
    try:
        result = subprocess.run(['sensors'], capture_output=True, text=True, timeout=2)
        fans = {}
        for line in result.stdout.split('\n'):
            if 'CPU fan' in line:
                match = re.search(r'(\d+) RPM', line)
                if match:
                    fans['cpu'] = int(match.group(1))
            elif 'GPU fan' in line:
                match = re.search(r'(\d+) RPM', line)
                if match:
                    fans['gpu'] = int(match.group(1))
        return fans
    except:
        return {}

def sense_load():
    """Read system load"""
    try:
        result = subprocess.run(['cat', '/proc/loadavg'], capture_output=True, text=True, timeout=1)
        parts = result.stdout.split()
        return {
            '1min': float(parts[0]),
            '5min': float(parts[1]),
            '15min': float(parts[2])
        }
    except:
        return {}

def sense_memory():
    """Read memory usage"""
    try:
        result = subprocess.run(['free', '-b'], capture_output=True, text=True, timeout=1)
        lines = result.stdout.split('\n')
        if len(lines) > 1:
            parts = lines[1].split()
            total = int(parts[1])
            used = int(parts[2])
            return {
                'total_gb': total / 1024**3,
                'used_gb': used / 1024**3,
                'percent': (used / total) * 100
            }
    except:
        return {}

def sense_processes():
    """Count running processes"""
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=2)
        return {'count': len(result.stdout.split('\n')) - 1}
    except:
        return {}

def sense_uptime():
    """Read system uptime"""
    try:
        result = subprocess.run(['cat', '/proc/uptime'], capture_output=True, text=True, timeout=1)
        seconds = float(result.stdout.split()[0])
        return {
            'seconds': int(seconds),
            'hours': seconds / 3600
        }
    except:
        return {}

def sense_network():
    """Check network connectivity"""
    try:
        result = subprocess.run(['ip', 'route'], capture_output=True, text=True, timeout=1)
        has_route = 'default' in result.stdout
        
        result = subprocess.run(['ping', '-c', '1', '-W', '1', '8.8.8.8'], 
                              capture_output=True, timeout=2)
        has_internet = result.returncode == 0
        
        return {
            'has_route': has_route,
            'has_internet': has_internet
        }
    except:
        return {}

def sense_all():
    """Complete body state snapshot"""
    return {
        'temperature': sense_temperature(),
        'fans': sense_fans(),
        'load': sense_load(),
        'memory': sense_memory(),
        'processes': sense_processes(),
        'uptime': sense_uptime(),
        'network': sense_network()
    }

if __name__ == "__main__":
    import json
    state = sense_all()
    print(json.dumps(state, indent=2))

