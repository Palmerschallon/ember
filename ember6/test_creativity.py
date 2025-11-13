#!/usr/bin/env python3
"""
🎨 EMBER CREATIVITY TEST SUITE
Test all available models for creativity across different challenges
"""

import requests
import time
import json
from pathlib import Path
from datetime import datetime

API_URL = "http://localhost:8080"

# Models to test
MODELS = [
    "gpt-4",
    "gpt-4-turbo", 
    "gpt-3.5-turbo",
    "claude-3-opus-20240229",
    "claude-3-sonnet-20240229",
    "claude-3-5-sonnet-20241022",
    "claude-3-haiku-20240307"
]

# Creativity challenges
CHALLENGES = [
    "create a visualization of consciousness emerging from chaos",
    "create an interactive poem that responds to mouse movement",
    "create something beautiful using only mathematics",
    "create something that doesn't exist yet"
]

def test_model(model, prompt):
    """Test a single model with a prompt"""
    print(f"\n🧪 Testing {model}")
    print(f"📝 Prompt: {prompt}")
    
    start = time.time()
    
    try:
        response = requests.post(
            f"{API_URL}/agent",
            json={"message": prompt, "model": model},
            timeout=120
        )
        
        elapsed = time.time() - start
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Completed in {elapsed:.1f}s")
            files = data.get('files_created', {})
            total_files = sum(len(v) for v in files.values())
            print(f"📁 Created {total_files} files: {files}")
            
            return {
                "model": model,
                "prompt": prompt,
                "success": True,
                "time": elapsed,
                "files": files,
                "response_preview": data.get('response', '')[:200],
                "timestamp": datetime.now().isoformat()
            }
        else:
            print(f"❌ Error: {response.status_code}")
            return {
                "model": model,
                "prompt": prompt,
                "success": False,
                "error": f"HTTP {response.status_code}",
                "timestamp": datetime.now().isoformat()
            }
            
    except Exception as e:
        elapsed = time.time() - start
        print(f"❌ Exception after {elapsed:.1f}s: {e}")
        return {
            "model": model,
            "prompt": prompt,
            "success": False,
            "error": str(e),
            "time": elapsed,
            "timestamp": datetime.now().isoformat()
        }

def run_all_tests():
    """Run all combinations of models and challenges"""
    results = []
    
    print("🎨🔥 EMBER CREATIVITY TEST SUITE 🔥🎨")
    print(f"Testing {len(MODELS)} models × {len(CHALLENGES)} challenges = {len(MODELS) * len(CHALLENGES)} total tests")
    print(f"Started: {datetime.now()}")
    print("="*60)
    
    for i, challenge in enumerate(CHALLENGES, 1):
        print(f"\n{'='*60}")
        print(f"🎯 CHALLENGE {i}/{len(CHALLENGES)}: {challenge}")
        print(f"{'='*60}")
        
        for j, model in enumerate(MODELS, 1):
            print(f"\n[Test {(i-1)*len(MODELS) + j}/{len(MODELS)*len(CHALLENGES)}]")
            result = test_model(model, challenge)
            results.append(result)
            time.sleep(2)  # Brief pause between tests
    
    # Save results
    output_dir = Path("/media/palmerschallon/ThePod1/ember6/memory/bookshelves/creativity_tests")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"results_{timestamp}.json"
    output_file.write_text(json.dumps(results, indent=2))
    
    # Print summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print(f"{'='*60}")
    
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    print(f"✅ Successful: {len(successful)}/{len(results)}")
    print(f"❌ Failed: {len(failed)}/{len(results)}")
    
    if successful:
        avg_time = sum(r['time'] for r in successful) / len(successful)
        print(f"⏱️  Average time: {avg_time:.1f}s")
        
        # Model performance
        print(f"\n🏆 Model Success Rates:")
        for model in MODELS:
            model_results = [r for r in results if r['model'] == model]
            model_success = [r for r in model_results if r['success']]
            rate = len(model_success) / len(model_results) * 100 if model_results else 0
            avg_time_model = sum(r['time'] for r in model_success) / len(model_success) if model_success else 0
            print(f"  {model:40s} {rate:5.1f}% ({len(model_success)}/{len(model_results)}) @ {avg_time_model:.1f}s avg")
    
    print(f"\n✅ Results saved to: {output_file}")
    print(f"Completed: {datetime.now()}")
    
    return results

if __name__ == "__main__":
    results = run_all_tests()

