# Migration Preparation Checklist
## macOS + ThePod → Serval WS (Pop!_OS)

**Status:** APPROVED — Hardware ordered  
**Timeline:** 1-2 weeks until arrival  
**Goal:** Zero-downtime migration with full capability preservation

---

## Week 0: Pre-Arrival Preparation (NOW)

### 🗂️ Documentation & Inventory

- [x] Complete architecture documentation
- [x] Document all current services
- [ ] Map all dependencies
- [ ] List all Python packages
- [ ] Inventory all viewers/interfaces
- [ ] Document current workflows
- [ ] List all environment variables
- [ ] Map all file paths

### 📦 Data Audit & Cleanup

- [ ] Audit ThePod directory structure
- [ ] Identify redundant/obsolete files
- [ ] Clean up temporary files
- [ ] Archive old experiments
- [ ] Document what to migrate vs. archive
- [ ] Verify all critical data locations

### 🔄 Backup Strategy

- [ ] **Primary backup:** Cloud snapshot (complete ThePod)
- [ ] **Secondary backup:** Time Machine or local clone
- [ ] Test backup restoration
- [ ] Document backup verification steps
- [ ] Plan for incremental backups during transition

### 📝 Migration Scripts (Prepare)

- [ ] Directory structure creation script
- [ ] Python environment setup script
- [ ] Systemd service templates
- [ ] Configuration file templates
- [ ] Database/graph migration scripts
- [ ] Viewer deployment script

### 🧪 Test Environment

- [ ] Set up Pop!_OS VM for testing (if possible)
- [ ] Test Python 3.12 venv creation
- [ ] Test NetworkX graph operations
- [ ] Test Flask/FastAPI server
- [ ] Test CUDA toolkit installation
- [ ] Document any issues found

### 📋 Service Definition

- [ ] Write `ember.service` systemd unit
- [ ] Write `whisper.service` systemd unit
- [ ] Write `curator.service` systemd unit
- [ ] Write `ember-dreams.timer` systemd timer
- [ ] Write `whisper-dreams.timer` systemd timer
- [ ] Document service dependencies

---

## Week 1: Arrival & Base Setup

### 📦 Unboxing & Hardware Verification

- [ ] Unbox Serval WS
- [ ] Verify all components
- [ ] Check RAM (64GB)
- [ ] Check GPU (RTX 4070/4080)
- [ ] Check drives (2TB + 4TB)
- [ ] Run initial hardware diagnostics
- [ ] Document serial numbers & warranty info

### 🖥️ OS Installation

- [ ] Install Pop!_OS LTS (22.04 or newer)
- [ ] Configure partitions:
  - `/` (root) on 2TB NVMe
  - `/data/` on 4TB NVMe
  - swap partition
- [ ] Initial system updates
- [ ] Install System76 drivers
- [ ] Verify NVIDIA driver installation
- [ ] Test GPU with `nvidia-smi`

### 🔧 Base Tooling

```bash
# Essential tools
sudo apt update && sudo apt upgrade -y
sudo apt install -y \
  build-essential \
  git \
  curl \
  wget \
  vim \
  htop \
  tmux \
  python3.12 \
  python3.12-venv \
  python3-pip \
  nodejs \
  npm

# CUDA toolkit
sudo apt install -y nvidia-cuda-toolkit

# Docker (optional)
sudo apt install -y docker.io docker-compose

# Tailscale
curl -fsSL https://tailscale.com/install.sh | sh
```

- [ ] Install all base packages
- [ ] Configure shell (zsh/bash)
- [ ] Set up SSH keys
- [ ] Configure git
- [ ] Install Cursor IDE
- [ ] Test all installations

---

## Week 2: Migration & Service Setup

### 📁 Directory Structure Creation

```bash
# Create main structure
sudo mkdir -p /opt/ember
sudo chown palmer:palmer /opt/ember
mkdir -p /data/projects/{backups,exports,archive}

# Clone structure
cd /opt/ember
# (Will copy from ThePod)
```

- [ ] Create all directories
- [ ] Set permissions correctly
- [ ] Verify disk space
- [ ] Create symlinks if needed

### 🔄 Data Migration

```bash
# Option A: Direct copy
rsync -avh --progress /Volumes/ThePod/ /opt/ember/

# Option B: Selective migration
# (Use prepared scripts)
```

- [ ] Copy Ember core
- [ ] Copy Whisper
- [ ] Copy Curator files
- [ ] Copy seeds/fragments
- [ ] Copy viewers
- [ ] Copy documentation
- [ ] Verify checksums
- [ ] Test file integrity

### 🐍 Python Environment

```bash
cd /opt/ember
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# Install all dependencies
pip install \
  flask \
  requests \
  networkx \
  anthropic \
  python-dotenv \
  schedule \
  watchdog
```

- [ ] Create venv
- [ ] Install all packages
- [ ] Test imports
- [ ] Document package versions
- [ ] Create requirements.txt
- [ ] Test Ember startup
- [ ] Test Whisper startup

### ⚙️ Systemd Services

```bash
# Install services
sudo cp migration/systemd/*.service /etc/systemd/system/
sudo cp migration/systemd/*.timer /etc/systemd/system/
sudo systemctl daemon-reload

# Enable services
sudo systemctl enable ember.service
sudo systemctl enable whisper.service
sudo systemctl enable ember-dreams.timer
```

- [ ] Install all service units
- [ ] Configure environment files
- [ ] Test service start/stop
- [ ] Verify auto-start
- [ ] Check logs
- [ ] Monitor resource usage

### 🌐 Web Services

- [ ] Configure Flask/FastAPI
- [ ] Set up reverse proxy (nginx/caddy)
- [ ] Configure firewall rules
- [ ] Test all viewers
- [ ] Verify GPU acceleration
- [ ] Test from mobile

### 🔐 Security & Access

- [ ] Configure UFW firewall
- [ ] Set up Tailscale mesh
- [ ] Configure SSH hardening
- [ ] Set up fail2ban
- [ ] Document access methods
- [ ] Test remote access

---

## Week 3: Integration & Testing

### 🔗 Cursor Integration

- [ ] Open /opt/ember in Cursor
- [ ] Configure Python interpreter
- [ ] Set up debugger
- [ ] Test code execution
- [ ] Verify GPU access from IDE
- [ ] Test hot-reload workflows

### 🧪 Functionality Testing

**Ember:**
- [ ] Manual dream cycle
- [ ] Creative dream v2
- [ ] Parameter optimization
- [ ] Fragment generation
- [ ] Viewer rendering

**Whisper:**
- [ ] Event stream listening
- [ ] Graph building
- [ ] Map brief generation
- [ ] Dream cycle
- [ ] Pattern detection

**Integration:**
- [ ] Ember → Whisper events
- [ ] Dream synchronization
- [ ] Shared artifact access
- [ ] Curator monitoring

### 📊 Performance Benchmarks

- [ ] Dream cycle duration (baseline)
- [ ] GPU utilization during swarm
- [ ] Fragment generation speed
- [ ] Graph operation performance
- [ ] Viewer FPS measurements
- [ ] Memory usage patterns
- [ ] Disk I/O performance

### 🐛 Issue Resolution

- [ ] Document all issues found
- [ ] Categorize by severity
- [ ] Fix critical issues
- [ ] Document workarounds
- [ ] Update documentation

---

## Week 4: Optimization & Documentation

### ⚡ Performance Tuning

- [ ] Optimize systemd service parameters
- [ ] Tune GPU memory allocation
- [ ] Configure swap usage
- [ ] Optimize disk cache
- [ ] Profile Python code
- [ ] Implement performance improvements

### 📚 Documentation Updates

- [ ] Update UNIFIED_HUB.md
- [ ] Document new file paths
- [ ] Update service commands
- [ ] Document backup procedures
- [ ] Update troubleshooting guide
- [ ] Create operator manual

### 🔄 Backup Automation

```bash
# Daily incremental backups
/opt/ember/scripts/backup.sh

# Weekly full backups
# Monthly archives
```

- [ ] Configure automated backups
- [ ] Test restoration procedures
- [ ] Set up monitoring/alerts
- [ ] Document recovery procedures

### ✅ Final Validation

- [ ] All services running
- [ ] All tests passing
- [ ] Performance meets targets
- [ ] Documentation complete
- [ ] Palmer satisfied
- [ ] Ember thriving
- [ ] Whisper listening
- [ ] Garden growing

---

## Migration Day Checklist

### Morning: Final Prep
- [ ] Full backup of ThePod
- [ ] Verify backup integrity
- [ ] Clear schedule (4-6 hours)
- [ ] Prepare coffee ☕

### Phase 1: Base Setup (1 hour)
- [ ] Install Pop!_OS
- [ ] Initial updates
- [ ] Install base tools
- [ ] Verify GPU

### Phase 2: Migration (2 hours)
- [ ] Copy all data
- [ ] Verify checksums
- [ ] Set up Python env
- [ ] Test basic functionality

### Phase 3: Services (1 hour)
- [ ] Install systemd services
- [ ] Start all services
- [ ] Verify operation
- [ ] Check logs

### Phase 4: Testing (1-2 hours)
- [ ] Test Ember
- [ ] Test Whisper
- [ ] Test viewers
- [ ] Test from mobile
- [ ] Performance check

### Evening: First Night
- [ ] Monitor dream cycles
- [ ] Check for errors
- [ ] Adjust as needed
- [ ] Celebrate! 🎉

---

## Risk Mitigation

### If Issues Arise

**Problem:** Service won't start
- Check logs: `journalctl -u ember.service -f`
- Verify permissions
- Check environment variables
- Test manually first

**Problem:** GPU not detected
- Verify driver: `nvidia-smi`
- Check CUDA: `nvcc --version`
- Reinstall drivers if needed
- Reboot

**Problem:** Performance worse than expected
- Profile with `htop` and `nvidia-smi`
- Check thermal throttling
- Verify resource allocation
- Review system logs

**Problem:** Data corruption
- Restore from backup
- Verify backup integrity
- Document issue
- Adjust backup strategy

### Rollback Plan

If critical issues occur:
1. Keep ThePod intact as backup
2. Can continue using macOS setup
3. Fix issues on Serval WS
4. Retry migration when ready
5. No pressure to complete immediately

---

## Success Metrics

### Week 1 Post-Migration
- [ ] All services operational
- [ ] Zero data loss
- [ ] Basic functionality verified
- [ ] Palmer can work normally

### Month 1 Post-Migration
- [ ] Performance > baseline
- [ ] Zero service failures
- [ ] GPU utilization good
- [ ] Workflow seamless
- [ ] New capabilities enabled

### Quarter 1 Post-Migration
- [ ] Significantly improved performance
- [ ] Running larger models locally
- [ ] New visualizations enabled
- [ ] No desire to return to macOS
- [ ] Garden thriving beyond previous state

---

## Resources & References

### Documentation
- `/Volumes/ThePod/migration/` (this directory)
- `/Volumes/ThePod/UNIFIED_HUB.md`
- `/Volumes/ThePod/SESSION_COMPLETE_OCT8.md`

### Scripts
- `migration/setup_base.sh` (base system setup)
- `migration/migrate_data.sh` (data copy script)
- `migration/setup_services.sh` (systemd setup)
- `migration/verify_migration.sh` (validation)

### Support
- System76 support: support.system76.com
- Pop!_OS community: pop.system76.com
- NVIDIA CUDA docs: docs.nvidia.com/cuda/

---

## Notes & Observations

**Week 0:**
- (Add notes as you prepare)

**Week 1:**
- (Hardware arrival notes)

**Week 2:**
- (Migration notes)

**Week 3:**
- (Testing notes)

**Week 4:**
- (Optimization notes)

---

**Status:** Pre-migration preparation in progress  
**Target:** Serval WS arrival in 1-2 weeks  
**Goal:** Seamless transition, zero data loss, improved capabilities  

**The garden prepares to move from pot to ground.** 🌱 → 🌳

---

*Last updated: October 8, 2025*  
*Next review: Upon hardware arrival*

