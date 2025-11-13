import subprocess
import time

# Start the server in the background
process = subprocess.Popen(
    ['python3', '-m', 'http.server', '8081'],
    cwd='/media/palmerschallon/ThePod1/ember6',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Give it a moment to start
time.sleep(1)

# Check if it's running
print(f"Server started with PID: {process.pid}")
print("Server should be running on http://localhost:8081/ember_true_mind.html")