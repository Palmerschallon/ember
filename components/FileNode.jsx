import React, { useState, useEffect } from 'react';
import { Handle } from 'reactflow';

export const FileNode = ({ data }) => {
  const [preview, setPreview] = useState('');
  const [fileStats, setFileStats] = useState(null);
  
  useEffect(() => {
    // Load real file preview
    loadFilePreview(data.path);
    loadFileStats(data.path);
  }, [data.path]);
  
  const loadFilePreview = async (path) => {
    try {
      const content = await window.electron.readFile(path);
      const preview = generatePreview(content, data.type);
      setPreview(preview);
    } catch (err) {
      setPreview('Unable to load preview');
    }
  };
  
  const loadFileStats = async (path) => {
    const stats = await window.electron.getFileStats(path);
    setFileStats(stats);
  };
  
  const handleDoubleClick = () => {
    window.electron.openInEditor(data.path);
  };
  
  const getFileIcon = (type) => {
    const icons = {
      python: '🐍',
      javascript: '⚡',
      html: '🌐',
      css: '🎨',
      image: '🖼️',
      json: '📋',
      markdown: '📝'
    };
    return icons[type] || '📄';
  };
  
  return (
    <div 
      className="file-node"
      onDoubleClick={handleDoubleClick}
      style={{
        background: `linear-gradient(135deg, ${data.color1}, ${data.color2})`,
        padding: '10px',
        borderRadius: '8px',
        minWidth: '150px',
        cursor: 'pointer'
      }}
    >
      <Handle type="target" position="left" />
      
      <div className="file-header">
        <span className="file-icon">{getFileIcon(data.type)}</span>
        <span className="file-name">{data.name}</span>
      </div>
      
      {preview && (
        <div className="file-preview">
          {data.type === 'image' ? 
            <img src={`file://${data.path}`} alt={data.name} /> :
            <pre>{preview}</pre>
          }
        </div>
      )}
      
      {fileStats && (
        <div className="file-stats">
          <span>{formatBytes(fileStats.size)}</span>
          <span>{formatDate(fileStats.mtime)}</span>
        </div>
      )}
      
      <Handle type="source" position="right" />
    </div>
  );
};

const generatePreview = (content, type) => {
  const MAX_PREVIEW_LENGTH = 100;
  
  if (type === 'image') return null; // Handle separately
  
  if (type === 'json') {
    try {
      const parsed = JSON.parse(content);
      return JSON.stringify(parsed, null, 2).substring(0, MAX_PREVIEW_LENGTH) + '...';
    } catch {
      return content.substring(0, MAX_PREVIEW_LENGTH) + '...';
    }
  }
  
  // For code files, try to get the first meaningful lines
  const lines = content.split('\n');
  const meaningfulLines = lines.filter(line => line.trim() && !line.trim().startsWith('#'));
  return meaningfulLines.slice(0, 3).join('\n');
};

const formatBytes = (bytes) => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

const formatDate = (date) => {
  return new Date(date).toLocaleDateString();
};