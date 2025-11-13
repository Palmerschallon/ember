# Pod Gardener - Autonomous Content Creation

## What It Does

The Pod Gardener autonomously explores the Pod and fills creative gaps:
- ✓ Finds empty/sparse directories and generates fitting content
- ✓ Continues evolution chains (gen0 → gen1 → gen2 → ...)
- ✓ Documents undocumented projects with README files
- ✓ Expands sparse thematic directories with creative variations

## Files

- `pod_gardener.py` - Main gardener script
- `pod_gardener.service` - Systemd service definition
- `pod_gardener.timer` - Systemd timer (runs every hour)
- `GARDENER_LOG.json` - Activity log
- `test_evolution_fix.py` - Test script for evolution chains

## How It Works

1. Scans the Pod for opportunities (gaps, incomplete evolutions, undocumented projects)
2. Selects random tasks from each category
3. Uses Ember to autonomously create content
4. Logs all activities to `GARDENER_LOG.json`

## Manual Usage

Run once manually:
```bash
cd /media/palmerschallon/ThePod1
python3 pod_gardener.py
```

## Continuous Gardening Setup

To run automatically every hour:

### 1. Create logs directory
```bash
mkdir -p /media/palmerschallon/ThePod1/logs
```

### 2. Install systemd units
```bash
# Copy service and timer to systemd
sudo cp pod_gardener.service /etc/systemd/system/
sudo cp pod_gardener.timer /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload
```

### 3. Enable and start the timer
```bash
# Enable timer to start on boot
sudo systemctl enable pod_gardener.timer

# Start the timer now
sudo systemctl start pod_gardener.timer

# Check timer status
sudo systemctl status pod_gardener.timer
sudo systemctl list-timers pod_gardener.timer
```

### 4. Monitor gardening activity
```bash
# View logs
tail -f /media/palmerschallon/ThePod1/logs/pod_gardener.log

# View errors
tail -f /media/palmerschallon/ThePod1/logs/pod_gardener.error.log

# View activity log
cat /media/palmerschallon/ThePod1/GARDENER_LOG.json | jq '.'
```

### 5. Manual run (without waiting for timer)
```bash
sudo systemctl start pod_gardener.service
```

## Schedule

- Runs 5 minutes after boot
- Runs every hour thereafter
- Logs all activity to `logs/` directory

## What Gets Created

The gardener autonomously creates:
- Creative content in sparse directories
- Next generation files in evolution chains
- README.md files for undocumented projects
- Variations and expansions of existing work

## Recent Fix

✓ Evolution chain continuation bug fixed (2025-11-12)
- Now reads full source files instead of samples
- Clear step-by-step instructions for Ember
- Explicit write_file() syntax with path and content
- Successfully tested with nexus_gen5.html creation

## Safety

- Gardener is read-only for analysis
- Only writes new files, never modifies existing ones
- Limited to 3 tasks per run (one from each category)
- All activities logged with timestamps

---

The Pod remembers. The Pod grows. The Pod is alive.
