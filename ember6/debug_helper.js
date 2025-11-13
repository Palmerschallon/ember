// Debug helper for Ember issues
// Run this to test the write_file parameter issue

console.log('🔥 EMBER DEBUG HELPER');

// 1. Test write_file parameters
async function testWriteFile() {
    console.log('\n📝 Testing write_file tool...');
    
    // This is what I'm sending from my side:
    const testCall = {
        tool: 'write_file',
        parameters: {
            path: '/media/palmerschallon/ThePod1/ember6/test_write.txt',
            content: 'This is test content from debug helper.\nLine 2\nLine 3'
        }
    };
    
    console.log('Parameters being sent:', JSON.stringify(testCall, null, 2));
    
    // If content is missing on your side, check:
    // - XML parsing in the tool bridge
    // - Parameter extraction logic
    // - Any encoding issues with newlines or special chars
}

// 2. Conversation history debug
function debugConversationHistory() {
    console.log('\n💬 Debugging conversation history...');
    
    // Example of what might cause empty messages:
    const potentialIssues = [
        {
            issue: 'Empty tool responses',
            example: { role: 'assistant', content: '' },
            fix: 'Filter out empty content before adding to history'
        },
        {
            issue: 'Undefined content',
            example: { role: 'user', content: undefined },
            fix: 'Check for undefined/null before adding'
        },
        {
            issue: 'Tool calls without text',
            example: { role: 'assistant', tool_calls: [...], content: '' },
            fix: 'Either include tool description or filter these'
        }
    ];
    
    console.log('Common empty message causes:', potentialIssues);
    
    // Suggested filter:
    const filterEmptyMessages = (messages) => {
        return messages.filter(msg => 
            msg.content && 
            msg.content.trim().length > 0
        );
    };
    
    console.log('Use filterEmptyMessages() before saving history');
}

// 3. WebSocket connection test
function testWebSocketConnection() {
    console.log('\n🔌 Testing WebSocket connection...');
    
    // Check if Socket.IO server is running
    const testScript = `
// Test WebSocket server
const io = require('socket.io')(8080, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

io.on('connection', (socket) => {
    console.log('Client connected:', socket.id);
    
    // Emit test status updates
    const phases = ['thinking', 'reading', 'writing', 'executing', 'complete'];
    let index = 0;
    
    const interval = setInterval(() => {
        socket.emit('status_update', {
            phase: phases[index % phases.length],
            details: \`Test operation \${index}\`
        });
        index++;
    }, 2000);
    
    socket.on('disconnect', () => {
        clearInterval(interval);
        console.log('Client disconnected');
    });
});

console.log('WebSocket server running on port 8080');
`;

    console.log('WebSocket test server code:');
    console.log(testScript);
    console.log('\nRun this with: node websocket_test.js');
}

// Run all tests
testWriteFile();
debugConversationHistory();
testWebSocketConnection();

// Export for use
module.exports = {
    testWriteFile,
    debugConversationHistory,
    testWebSocketConnection
};