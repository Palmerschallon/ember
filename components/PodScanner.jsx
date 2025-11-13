import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';

export const PodScanner = ({ onScanComplete }) => {
  const [scanning, setScanning] = useState(false);
  const [currentPath, setCurrentPath] = useState('');
  const [foundItems, setFoundItems] = useState([]);
  const [fileTree, setFileTree] = useState({});
  
  const scanPod = async () => {
    setScanning(true);
    setFoundItems([]);
    
    // Start with Pod root
    const podPath = '/media/palmerschallon/ThePod1';
    await scanDirectory(podPath, '');
    
    setScanning(false);
    onScanComplete?.(fileTree);
  };
  
  const scanDirectory = async (path, relativePath) => {
    setCurrentPath(path);
    
    try {
      const items = await window.electron.readdir(path);
      
      for (const item of items) {
        const fullPath = `${path}/${item}`;
        const stats = await window.electron.stat(fullPath);
        
        const fileInfo = {
          name: item,
          path: fullPath,
          relativePath: `${relativePath}/${item}`,
          type: getFileType(item),
          size: stats.size,
          modified: stats.mtime,
          isDirectory: stats.isDirectory()
        };
        
        // Add to found items for live display
        setFoundItems(prev => [...prev, fileInfo]);
        
        // Build tree structure
        setFileTree(prev => ({
          ...prev,
          [fileInfo.relativePath]: fileInfo
        }));
        
        // Recursively scan subdirectories (but skip hidden and node_modules)
        if (stats.isDirectory() && !item.startsWith('.') && item !== 'node_modules') {
          await scanDirectory(fullPath, `${relativePath}/${item}`);
        }
        
        // Small delay for visual effect
        await new Promise(resolve => setTimeout(resolve, 10));
      }
    } catch (err) {
      console.error(`Error scanning ${path}:`, err);
    }
  };
  
  const getFileType = (filename) => {
    const ext = filename.split('.').pop().toLowerCase();
    const typeMap = {
      'py': 'python',
      'js': 'javascript',
      'jsx': 'react',
      'html': 'html',
      'css': 'style',
      'json': 'data',
      'md': 'markdown',
      'png': 'image',
      'jpg': 'image',
      'gif': 'image',
      'svg': 'vector'
    };
    return typeMap[ext] || 'file';
  };
  
  const getFileIcon = (type) => {
    const icons = {
      'python': '🐍',
      'javascript': '⚡',
      'react': '⚛️',
      'html': '🌐',
      'style': '🎨',
      'data': '📊',
      'markdown': '📝',
      'image': '🖼️',
      'vector': '🎯',
      'file': '📄',
      'directory': '📁'
    };
    return icons[type] || '📄';
  };
  
  return (
    <div className="pod-scanner">
      <div className="scanner-header">
        <h3>Pod Scanner</h3>
        <button 
          onClick={scanPod} 
          disabled={scanning}
          className="scan-button"
        >
          {scanning ? 'Scanning...' : 'Scan The Pod'}
        </button>
      </div>
      
      {scanning && (
        <div className="scanning-display">
          <motion.div 
            className="scan-line"
            animate={{ 
              y: [0, 200, 0],
              opacity: [0.3, 1, 0.3]
            }}
            transition={{ 
              repeat: Infinity, 
              duration: 2 
            }}
            style={{
              height: '2px',
              background: 'linear-gradient(90deg, transparent, #00ff00, transparent)',
              position: 'absolute',
              width: '100%'
            }}
          />
          
          <div className="current-scan">
            <span className="scan-icon">🔍</span>
            <span className="scan-path">{currentPath}</span>
          </div>
        </div>
      )}
      
      <div className="found-items">
        {foundItems.slice(-10).map((item, index) => (
          <motion.div
            key={item.path}
            className="found-item"
            initial={{ x: -50, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ delay: index * 0.05 }}
            style={{
              padding: '8px',
              borderLeft: '3px solid #00ff00',
              marginBottom: '4px',
              background: 'rgba(0, 255, 0, 0.05)'
            }}
          >
            <span className="item-icon">{getFileIcon(item.isDirectory ? 'directory' : item.type)}</span>
            <span className="item-name">{item.name}</span>
            <span className="item-size">{formatBytes(item.size)}</span>
          </motion.div>
        ))}
      </div>
      
      {!scanning && foundItems.length > 0 && (
        <div className="scan-summary">
          <h4>Scan Complete!</h4>
          <div className="stats">
            <div className="stat">
              <span className="stat-value">{foundItems.length}</span>
              <span className="stat-label">Total Files</span>
            </div>
            <div className="stat">
              <span className="stat-value">{foundItems.filter(f => f.isDirectory).length}</span>
              <span className="stat-label">Directories</span>
            </div>
            <div className="stat">
              <span className="stat-value">{formatBytes(foundItems.reduce((sum, f) => sum + f.size, 0))}</span>
              <span className="stat-label">Total Size</span>
            </div>
          </div>
          
          <div className="file-types">
            {Object.entries(
              foundItems.reduce((acc, item) => {
                if (!item.isDirectory) {
                  acc[item.type] = (acc[item.type] || 0) + 1;
                }
                return acc;
              }, {})
            ).map(([type, count]) => (
              <div key={type} className="type-badge">
                {getFileIcon(type)} {type}: {count}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

const formatBytes = (bytes) => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

// Electron preload script would need:
// contextBridge.exposeInMainWorld('electron', {
//   readdir: (path) => ipcRenderer.invoke('readdir', path),
//   stat: (path) => ipcRenderer.invoke('stat', path)
// });