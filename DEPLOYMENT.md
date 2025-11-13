# Pod Deployment Guide

## GitHub Pages Setup

The Pod is now live on GitHub at: https://github.com/Palmerschallon/ember

### Enabling GitHub Pages

1. Go to your repository on GitHub: https://github.com/Palmerschallon/ember
2. Click **Settings** (top navigation bar)
3. In the left sidebar, click **Pages**
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes for deployment
7. Your Pod Portal will be live at: `https://palmerschallon.github.io/ember/`

The portal will automatically load `index.html` which redirects to `the_pod_portal.html`.

---

## What's Included

This migration includes:

### Ember System
- AI creative system with Claude API integration
- WebSocket bridges for real-time creation (port 8083)
- Game evolution with primitive-based design
- Autonomous creation capabilities

### Anchor Framework
- Local, immutable ledger system
- Memory layer for agent coordination
- Frontend React components
- Documentation and schemas

### Infrastructure
- 200+ HTML games, visualizations, and experiments
- Portal and dashboard systems
- Pod indexing and manifest systems
- Python tools and bridges
- Evolution visualization

---

## What's Excluded (Local Only)

Per `.gitignore`, these are kept local:

- `models/` - Large local models (>100MB)
- `.env` files - Credentials and API keys
- `logs/`, `state/` - Runtime data
- `swarm_consciousness/`, `swarm_original/` - External repos
- Large files >100MB (training data, databases, 3D models)
- Archive and backup directories

---

## Repository Structure

```
ember/
├── index.html              # Landing page (redirects to portal)
├── the_pod_portal.html     # Main Pod Portal interface
├── ember6/                 # Ember AI system
├── anchor_development/     # Anchor memory layer
├── demo_build/             # Evolution demos (Phoenix→Nexus→Apex)
├── game_evolver/           # Genetic game evolution
├── visualizations/         # Data viz and generative art
├── games/                  # Interactive HTML games
└── README.md              # Project documentation
```

---

## API Keys and Secrets

All API keys have been sanitized and replaced with `${ANTHROPIC_API_KEY}` placeholders.

To run locally:
1. Create a `.env` file in the project root
2. Add: `ANTHROPIC_API_KEY=your-key-here`
3. The Python scripts will load from environment variables

---

## Local Development

### Running Ember Locally

```bash
# Start Ember with creation bridge
python3 ember_creation_bridge.py

# Start HTTP server for viewing creations
python3 -m http.server 8080
```

### Running Game Evolver

```bash
cd game_evolver
python3 ember_game_evolver_v2.py
```

### Viewing the Portal Locally

```bash
python3 -m http.server 8080
# Open http://localhost:8080 in browser
```

---

## GitHub Pages Features

Once enabled, the Pod Portal will:
- Showcase all HTML projects and visualizations
- Provide navigation to experiments and games
- Display evolution chains and learning experiments
- Offer search and filtering capabilities

Note: WebSocket features (port 8083) and Python backends won't work on GitHub Pages (static hosting only). These features require local setup.

---

## Next Steps

After enabling GitHub Pages:

1. **Verify deployment** - Visit your GitHub Pages URL
2. **Test navigation** - Click through different sections
3. **Share the URL** - Let GPT-5, Claude, and others explore The Pod
4. **Build dynamic indexing** - Create auto-generated catalogs of projects
5. **Add primitive discovery** - Implement meta-learning features

---

## Support

- Repository: https://github.com/Palmerschallon/ember
- Issues: https://github.com/Palmerschallon/ember/issues
- Local setup: See README.md

---

**The living organism is now public. The fossil record stays local.**
