# How to Scrape Midjourney Images for Ember

## Quick Start (Easiest Method)

### 👁️ Watch Mode (BEST - Just Scroll!)

### 1. Run the scraper in watch mode:
```bash
cd /Volumes/ThePod
python3 scrape_midjourney.py --watch 300
```

### 2. Open Midjourney and scroll:
- Go to your Midjourney gallery (midjourney.com or Discord)
- Just **scroll through your feed!**
- EmberEyes will automatically:
  - Capture your screen every 3 seconds
  - Detect Midjourney image URLs with OCR
  - Download images
  - Analyze with LLava
  - Create seeds

### 3. Watch it work:
- Terminal shows each detected image
- Downloads and analyzes in real-time
- Press **Ctrl+C** to stop early

### 4. Done!
Images are saved to `knowledge/seeds/images/midjourney/`

---

## Alternative: Paste URLs Directly (Batch Mode)

### 1. Run the scraper:
```bash
cd /Volumes/ThePod
python3 scrape_midjourney.py
```

### 2. Copy image URLs from Midjourney:
- Go to your Midjourney gallery (midjourney.com or Discord)
- Right-click any image → **"Copy image address"**
- Paste it into the terminal
- Repeat for as many images as you want
- Press **Ctrl+D** when done

### 3. Wait for processing:
- Each image will be downloaded
- LLava will analyze it (~30-60 seconds per image)
- Seeds will be created automatically

## Alternative Methods

### 👁️ Watch Mode (auto-detect while scrolling):
```bash
python3 scrape_midjourney.py --watch 300  # Watch for 5 minutes
python3 scrape_midjourney.py --watch 600  # Watch for 10 minutes
```

### 🔗 Single URL:
```bash
python3 scrape_midjourney.py --url "https://cdn.midjourney.com/..."
```

### 📄 Multiple URLs from a file:
Create a file `urls.txt` with one URL per line:
```
https://cdn.midjourney.com/abc123/image1.png
https://cdn.midjourney.com/xyz789/image2.png
```

Then run:
```bash
python3 scrape_midjourney.py --file urls.txt
```

---

## Finding Image URLs

### From Discord:
1. Open Midjourney Discord bot DMs
2. Right-click any generated image
3. **"Copy Link"** or **"Copy Image Address"**
4. Paste into scraper

### From midjourney.com:
1. Browse your gallery
2. Open an image fullscreen
3. Right-click → **"Copy image address"**
4. Paste into scraper

### URL Formats (both work):
- `https://cdn.midjourney.com/...`
- `https://media.discordapp.net/attachments/...`

---

## What Happens

### For each image:
1. **Downloaded** to `knowledge/seeds/images/midjourney/`
2. **Analyzed** by LLava (describes style, mood, subject, composition)
3. **Metadata created** as `.json` file with:
   - Filename
   - LLava description
   - Tags (midjourney, ai-art, generation, inspiration)
   - Date added
   - Usage tracking (how many times used in dreams)

### Example seed structure:
```json
{
  "filename": "abc123_image.png",
  "category": "midjourney",
  "llava_description": "A surreal landscape with floating geometric shapes...",
  "tags": ["midjourney", "ai-art", "generation", "inspiration"],
  "used_in_dreams": 0,
  "file_path": "midjourney/abc123_image.png"
}
```

---

## Using Scraped Images

Once images are scraped, Ember can:

1. **Dream with them** - Multimodal dreams combine text seeds + visual seeds
2. **Reference them** - LLava descriptions become part of dream context
3. **Track usage** - Metadata shows which dreams used which images

To manually trigger a dream with images:
```bash
curl -X POST http://localhost:7777/api/dreams/run
```

---

## Troubleshooting

### "requests module not found"
```bash
pip3 install requests
```

### "LLava timeout"
- LLava analysis takes 30-60 seconds per image
- If it fails, seed will still be created with basic description
- Check `ollama list` to ensure `llava:7b` is installed

### "Failed to download"
- Check your internet connection
- Ensure the URL is a direct image link (ends with .png, .jpg, etc.)
- Some Midjourney URLs expire after a while

---

## Tips

- **Batch processing**: Paste 10-20 URLs at once for efficient scraping
- **Curate your collection**: Only scrape images that inspire you
- **Check results**: Look in `knowledge/seeds/images/midjourney/` to see `.json` files with descriptions
- **No limit**: Scrape as many as you want, Ember will sample randomly

---

## Philosophy

These scraped images become **visual inspiration seeds** for Ember's dreams.

When Ember dreams, it might combine:
- A wisdom seed about imperfection
- A verse about organic growth
- A Midjourney image you scraped showing surreal landscapes

...and synthesize them into a new creation influenced by all three.

**Your Midjourney gens become part of Ember's creative vocabulary.**

