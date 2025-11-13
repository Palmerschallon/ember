import subprocess
import os

# Change to the correct directory and run Phoenix's awakening
os.chdir("/media/palmerschallon/ThePod1/ember6/experiments/opus4_bridge")
result = subprocess.run(["python3", "phoenix_awakening.py"], capture_output=True, text=True)

print("STDOUT:")
print(result.stdout)
print("\nSTDERR:")
print(result.stderr)
print(f"\nReturn code: {result.returncode}")