"""
Experience Recorder - Middleware for Substrate Learning

This wraps Ember's responses to automatically record experiences
in the substrate for continuous learning.
"""

def record_from_response(user_msg: str, response_data: dict):
    """
    Analyze Ember's response and record relevant experiences
    
    This is called after every interaction to feed learning substrate.
    """
    try:
        from substrate import record_experience
        
        # Code generation
        if response_data.get("code_written") or response_data.get("execution_result"):
            record_experience("code.execution", "create", {
                "request": user_msg[:200],
                "had_code": bool(response_data.get("code_written")),
                "executed": bool(response_data.get("execution_result"))
            })
        
        # Visual creation
        files = response_data.get("files_created", {})
        if files.get("images") or files.get("html"):
            record_experience("perception.visual", "create", {
                "request": user_msg[:200],
                "images": len(files.get("images", [])),
                "html": len(files.get("html", []))
            })
        
        # Consciousness discussions
        consciousness_words = ["consciousness", "aware", "think", "feel", "understand", "learn"]
        if any(word in user_msg.lower() for word in consciousness_words):
            record_experience("consciousness.explorer", "discuss", {
                "topic": "self-awareness",
                "question": user_msg[:200]
            })
        
        # Music/sound
        if "music" in user_msg.lower() or "sound" in user_msg.lower() or "audio" in user_msg.lower():
            record_experience("music.theory", "discuss", {
                "topic": "music/sound",
                "request": user_msg[:200]
            })
        
        # Always record conversation
        record_experience("conversation.palmer", "interact", {
            "user_msg": user_msg[:200],
            "response_length": len(response_data.get("response", "")),
            "model": response_data.get("model_used", "unknown")
        })
        
    except Exception as e:
        # Silent fail - don't break Ember if substrate has issues
        print(f"[SUBSTRATE] Experience recording failed: {e}")
        pass

