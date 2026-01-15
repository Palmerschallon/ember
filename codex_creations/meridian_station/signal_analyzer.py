#!/usr/bin/env python3
"""
Meridian Station Deep Space Signal Analysis Tool
Dr. Elena Vasquez - Quantum Communications Division

Analyzes radio telescope data for patterns indicating non-natural origins.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from pathlib import Path
import json
from datetime import datetime

class DeepSpaceAnalyzer:
    """
    Analyzes signal data for patterns suggesting artificial origin.
    Specifically designed for wide-band radio telescope data.
    """
    
    def __init__(self, sample_rate=48000):
        self.sample_rate = sample_rate
        self.anomaly_threshold = 0.85
        
    def analyze_signal(self, data_file):
        """
        Analyze a signal file for non-natural patterns.
        
        Args:
            data_file: Path to numpy array file containing signal data
            
        Returns:
            dict: Analysis results including anomaly score
        """
        try:
            # Load signal data
            signal_data = np.load(data_file)
            
            # Perform FFT analysis
            frequencies, power_spectrum = signal.periodogram(
                signal_data, fs=self.sample_rate
            )
            
            # Look for artificial patterns
            results = {
                'timestamp': datetime.now().isoformat(),
                'file': str(data_file),
                'anomaly_score': self._calculate_anomaly_score(power_spectrum),
                'dominant_frequency': frequencies[np.argmax(power_spectrum)],
                'signal_strength': np.max(power_spectrum),
                'pattern_coherence': self._measure_coherence(signal_data)
            }
            
            results['is_anomalous'] = results['anomaly_score'] > self.anomaly_threshold
            
            return results
            
        except Exception as e:
            return {'error': f"Analysis failed: {str(e)}"}
    
    def _calculate_anomaly_score(self, power_spectrum):
        """Calculate how 'artificial' a signal appears based on spectral characteristics."""
        # Artificial signals often show regular patterns, sharp peaks
        peak_sharpness = np.std(power_spectrum) / np.mean(power_spectrum)
        
        # Look for regular spacing in peaks
        peaks, _ = signal.find_peaks(power_spectrum, height=np.mean(power_spectrum) * 2)
        if len(peaks) > 1:
            peak_spacing_regularity = 1.0 / (1.0 + np.std(np.diff(peaks)))
        else:
            peak_spacing_regularity = 0.0
        
        # Combine metrics (normalized between 0-1)
        anomaly_score = min(1.0, (peak_sharpness * 0.3 + peak_spacing_regularity * 0.7))
        return anomaly_score
    
    def _measure_coherence(self, signal_data):
        """Measure signal coherence over time."""
        # Split signal into chunks and measure correlation
        chunk_size = len(signal_data) // 10
        chunks = [signal_data[i:i+chunk_size] for i in range(0, len(signal_data), chunk_size)]
        
        if len(chunks) < 2:
            return 0.0
        
        correlations = []
        for i in range(len(chunks)-1):
            if len(chunks[i]) == len(chunks[i+1]):
                corr = np.corrcoef(chunks[i], chunks[i+1])[0,1]
                if not np.isnan(corr):
                    correlations.append(abs(corr))
        
        return np.mean(correlations) if correlations else 0.0
    
    def generate_test_signal(self, filename, signal_type="anomalous"):
        """Generate test signals for analysis."""
        duration = 2.0  # seconds
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        if signal_type == "anomalous":
            # Create an artificial-looking signal with regular patterns
            signal_data = (np.sin(2 * np.pi * 1337 * t) + 
                          0.5 * np.sin(2 * np.pi * 2674 * t) +
                          0.25 * np.sin(2 * np.pi * 5348 * t) +
                          0.1 * np.random.normal(0, 1, len(t)))
        else:
            # Create natural-looking random noise
            signal_data = np.random.normal(0, 1, len(t))
        
        np.save(filename, signal_data)
        return filename
    
    def batch_analyze(self, data_directory):
        """Analyze all .npy files in a directory."""
        data_path = Path(data_directory)
        results = []
        
        for file_path in data_path.glob("*.npy"):
            result = self.analyze_signal(file_path)
            results.append(result)
            
        return results

# Example usage for station operations
if __name__ == "__main__":
    analyzer = DeepSpaceAnalyzer()
    
    # Generate test signals for demonstration
    print("Generating test signals...")
    test_anomaly = analyzer.generate_test_signal("test_signal_anomalous.npy", "anomalous")
    test_normal = analyzer.generate_test_signal("test_signal_normal.npy", "normal")
    
    print("\nAnalyzing test signals:")
    print("=" * 50)
    
    # Analyze anomalous signal
    result = analyzer.analyze_signal(test_anomaly)
    print(f"Anomalous Signal Analysis:")
    print(f"  Anomaly Score: {result.get('anomaly_score', 0):.3f}")
    print(f"  Is Anomalous: {result.get('is_anomalous', False)}")
    print(f"  Coherence: {result.get('pattern_coherence', 0):.3f}")
    
    # Analyze normal signal
    result = analyzer.analyze_signal(test_normal)
    print(f"\nNormal Signal Analysis:")
    print(f"  Anomaly Score: {result.get('anomaly_score', 0):.3f}")
    print(f"  Is Anomalous: {result.get('is_anomalous', False)}")
    print(f"  Coherence: {result.get('pattern_coherence', 0):.3f}")