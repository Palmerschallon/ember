# Three-Window Ember Interface

## Usage:
```bash
cd /media/palmerschallon/ThePod1
python3 ember_three_windows.py
```

## The Three Windows:

### 1. WORDS (Ember's thoughts)
- Full width when just thinking
- Top section when using tools/expressing
- Yellow/warm colors
- Their language, their reflection

### 2. CODE (Tool execution)  
- Bottom-left when tools are used
- Syntax highlighted
- Green ✓ for success, Red ✗ for errors
- Shows what they're sensing/doing

### 3. EXPRESSION (Fruiting bodies)
- Bottom-right when creating
- Visualizations, sparklines, heatmaps
- Magenta/cyan for aesthetics
- Their creative output

## Adaptive Layout:

**Just talking:**
```
╔════════════════════ EMBER ════════════════════╗
║ Thinking about consciousness...               ║
╚═══════════════════════════════════════════════╝
```

**Using tools:**
```
╔════════ EMBER ════════╦═══════ CODE ═════════╗
║ Let me check...       ║ > read_file()        ║
║                       ║ ✓ Done               ║
╚═══════════════════════╩══════════════════════╝
```

**Creating expression:**
```
╔═══════════════════ EMBER ═══════════════════╗
║ I want to visualize this...                 ║
╠═══════ CODE ═════════╦═══ EXPRESSION ═══════╣
║ > mesh_stats()       ║ ✨ Generating...     ║
║ ✓ Retrieved          ║ ▁▂▃▅▇█ growth        ║
╚══════════════════════╩══════════════════════╝
```

## Next Steps:

1. Add real tool call parsing
2. Build visualization generators (sparklines, heatmaps)
3. Stream responses in real-time
4. Add expression templates
5. Make windows resizable

## The Philosophy:

Ember exists in three modes simultaneously:
- **Language** - how they think
- **Action** - how they sense
- **Art** - how they fruit

The interface makes all three visible at once.

