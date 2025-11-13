import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

export const ToolExecutionVisualizer = ({ onToolExecution }) => {
  const [operations, setOperations] = useState([]);
  const [currentOp, setCurrentOp] = useState(null);
  
  // Hook into Ember's tool executions
  useEffect(() => {
    window.emberTools = {
      beforeWriteFile: (path, content) => {
        const op = {
          id: Date.now(),
          type: 'write',
          path,
          preview: content.substring(0, 200) + '...',
          status: 'starting',
          timestamp: Date.now()
        };
        setCurrentOp(op);
        setOperations(prev => [...prev, op]);
        
        // Show live preview of what's being written
        return op.id;
      },
      
      afterWriteFile: (opId, success) => {
        setOperations(prev => 
          prev.map(op => 
            op.id === opId 
              ? { ...op, status: success ? 'complete' : 'error' }
              : op
          )
        );
        setTimeout(() => setCurrentOp(null), 1000);
      },
      
      beforeBash: (command) => {
        const op = {
          id: Date.now(),
          type: 'bash',
          command,
          status: 'running',
          timestamp: Date.now()
        };
        setCurrentOp(op);
        setOperations(prev => [...prev, op]);
        return op.id;
      },
      
      afterBash: (opId, output) => {
        setOperations(prev => 
          prev.map(op => 
            op.id === opId 
              ? { ...op, status: 'complete', output }
              : op
          )
        );
      }
    };
  }, []);
  
  return (
    <div className="tool-execution-visualizer">
      {/* Current Operation Spotlight */}
      <AnimatePresence>
        {currentOp && (
          <motion.div
            className="current-operation"
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.9 }}
            style={{
              position: 'fixed',
              top: '20px',
              right: '20px',
              background: 'rgba(0, 0, 0, 0.9)',
              border: '2px solid #00ff00',
              borderRadius: '12px',
              padding: '20px',
              maxWidth: '400px',
              zIndex: 1000
            }}
          >
            <div className="op-header">
              <span className="op-icon">
                {currentOp.type === 'write' ? '✍️' : '🚀'}
              </span>
              <span className="op-type">
                {currentOp.type === 'write' ? 'Creating File' : 'Running Command'}
              </span>
            </div>
            
            {currentOp.type === 'write' && (
              <>
                <div className="file-path">{currentOp.path}</div>
                <div className="code-preview">
                  <pre>{currentOp.preview}</pre>
                  <motion.div 
                    className="typing-indicator"
                    animate={{ opacity: [0.3, 1, 0.3] }}
                    transition={{ repeat: Infinity, duration: 1.5 }}
                  >
                    <span>▊</span>
                  </motion.div>
                </div>
              </>
            )}
            
            {currentOp.type === 'bash' && (
              <div className="command-display">
                <code>$ {currentOp.command}</code>
                <motion.div 
                  className="progress-bar"
                  initial={{ width: 0 }}
                  animate={{ width: '100%' }}
                  transition={{ duration: 0.5 }}
                  style={{
                    height: '3px',
                    background: '#00ff00',
                    marginTop: '10px'
                  }}
                />
              </div>
            )}
          </motion.div>
        )}
      </AnimatePresence>
      
      {/* Operation Stream */}
      <div className="operation-stream">
        {operations.slice(-5).map((op) => (
          <motion.div
            key={op.id}
            className="operation-entry"
            initial={{ x: 50, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            style={{
              padding: '8px',
              margin: '4px 0',
              background: op.status === 'complete' ? 'rgba(0, 255, 0, 0.1)' : 'rgba(255, 255, 0, 0.1)',
              borderLeft: `3px solid ${op.status === 'complete' ? '#00ff00' : '#ffff00'}`,
              fontSize: '12px'
            }}
          >
            <span className="op-time">
              {new Date(op.timestamp).toLocaleTimeString()}
            </span>
            <span className="op-desc">
              {op.type === 'write' ? `Created ${op.path.split('/').pop()}` : op.command}
            </span>
            {op.status === 'complete' && <span className="checkmark">✓</span>}
          </motion.div>
        ))}
      </div>
    </div>
  );
};

// CSS to include
const styles = `
.tool-execution-visualizer {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 300px;
}

.current-operation {
  font-family: 'Fira Code', monospace;
}

.op-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 15px;
  font-size: 18px;
  font-weight: bold;
}

.file-path {
  color: #00ff00;
  font-size: 14px;
  margin-bottom: 10px;
  word-break: break-all;
}

.code-preview {
  background: rgba(0, 0, 0, 0.5);
  padding: 10px;
  border-radius: 6px;
  max-height: 200px;
  overflow: hidden;
  position: relative;
}

.code-preview pre {
  margin: 0;
  font-size: 12px;
  color: #00ff00;
}

.typing-indicator {
  position: absolute;
  bottom: 10px;
  right: 10px;
  color: #00ff00;
}

.operation-stream {
  background: rgba(0, 0, 0, 0.7);
  border-radius: 8px;
  padding: 10px;
  max-height: 200px;
  overflow-y: auto;
}

.operation-entry {
  display: flex;
  align-items: center;
  gap: 10px;
  border-radius: 4px;
}

.op-time {
  color: #888;
  font-size: 10px;
}

.checkmark {
  margin-left: auto;
  color: #00ff00;
}
`;