#!/bin/bash
# Ember's Expansion - Install Creative Tools
# Palmer runs this when ready to give Ember creation capabilities

echo ""
echo "======================================================================"
echo "                   EMBER'S CREATIVE TOOLS"
echo "======================================================================"
echo ""

echo "This script installs programs for Ember to create with:"
echo "  - Blender (3D modeling/animation)"
echo "  - GIMP (image editing)"
echo "  - Inkscape (vector graphics)"
echo "  - scrot (screen capture)"
echo "  - ffmpeg (video processing)"
echo ""

read -p "Install all creative tools? (y/n): " choice

if [ "$choice" != "y" ]; then
    echo "Installation cancelled."
    exit 0
fi

echo ""
echo "Installing..."
echo ""

# Update package list
sudo apt update

# Install Blender
echo "[1/5] Installing Blender..."
sudo apt install -y blender

# Install GIMP
echo "[2/5] Installing GIMP..."
sudo apt install -y gimp

# Install Inkscape  
echo "[3/5] Installing Inkscape..."
sudo apt install -y inkscape

# Install scrot for screenshots
echo "[4/5] Installing scrot..."
sudo apt install -y scrot

# Install ffmpeg
echo "[5/5] Installing ffmpeg..."
sudo apt install -y ffmpeg

echo ""
echo "======================================================================"
echo "                      INSTALLATION COMPLETE"
echo "======================================================================"
echo ""

echo "Ember now has access to:"
echo "  ✓ Blender - 3D creation"
echo "  ✓ GIMP - Image editing"
echo "  ✓ Inkscape - Vector graphics"
echo "  ✓ scrot - Screen awareness"
echo "  ✓ ffmpeg - Video creation"
echo ""

echo "Testing installations..."
echo ""

blender --version | head -1
gimp --version | head -1
inkscape --version | head -1
scrot --version 2>&1 | head -1
ffmpeg -version | head -1

echo ""
echo "Ember is ready to create."
echo ""

