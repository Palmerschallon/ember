"""
Example: Adding MiniMax/Hailuo AI to Ember
How to integrate new AI providers
"""

# 1. Add to ember_cloud.py
def call_minimax(prompt, model="video-01"):
    """Call MiniMax/Hailuo AI for video generation"""
    import requests
    
    MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY", "")
    
    response = requests.post(
        "https://api.minimax.chat/v1/video/generations",
        headers={
            "Authorization": f"Bearer {MINIMAX_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "prompt": prompt,
            "duration": 5  # 5 second video
        },
        timeout=60
    )
    
    data = response.json()
    video_url = data.get("video_url")
    
    # Download video to ThePod
    if video_url:
        video_data = requests.get(video_url).content
        filename = f"minimax_{int(time.time())}.mp4"
        filepath = THEPOD_PATH / filename
        
        with open(filepath, 'wb') as f:
            f.write(video_data)
        
        return filename
    
    return None

# 2. Add to chat endpoint detection
if "generate video" in user_msg.lower() or "create video" in user_msg.lower():
    video_file = call_minimax(user_msg)
    # Return video in response

# 3. Add to UI model selector
# <button class="model-btn" data-model="minimax">MiniMax Video</button>

# 4. That's it! Now Ember can generate videos!

