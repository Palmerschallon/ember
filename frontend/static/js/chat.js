/**
 * Chat Interface
 */
class ChatInterface {
    constructor() {
        this.messagesContainer = document.getElementById('chat-messages');
        this.input = document.getElementById('chat-input');
        this.sendButton = document.getElementById('chat-send');
        this.history = [];
        
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        this.sendButton.addEventListener('click', () => this.sendMessage());
        this.input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
    }
    
    async sendMessage() {
        const message = this.input.value.trim();
        if (!message) return;
        
        // Clear input
        this.input.value = '';
        
        // Add user message to UI
        this.addMessage('user', message);
        
        // Send to backend
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message,
                    history: this.history
                })
            });
            
            const data = await response.json();
            
            // Add assistant response to UI
            this.addMessage('assistant', data.response);
            
            // Update history
            this.history.push(
                { role: 'user', content: message },
                { role: 'assistant', content: data.response }
            );
            
            // Keep history limited
            if (this.history.length > 20) {
                this.history = this.history.slice(-20);
            }
        } catch (error) {
            console.error('Chat error:', error);
            this.addMessage('assistant', 'Error: Could not reach the server.');
        }
    }
    
    addMessage(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${role}`;
        
        const roleDiv = document.createElement('div');
        roleDiv.className = 'role';
        roleDiv.textContent = role === 'user' ? 'You' : 'Assistant';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'content';
        contentDiv.textContent = content;
        
        messageDiv.appendChild(roleDiv);
        messageDiv.appendChild(contentDiv);
        
        this.messagesContainer.appendChild(messageDiv);
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }
}
