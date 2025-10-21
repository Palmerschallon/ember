#!/usr/bin/env python3
"""
EMBER AWARENESS WRAPPER

Wraps Ember/Swarm's actions to automatically surface relevant tabs.

When Ember works on memory → Memory tab surfaces
When Ember searches → Sky window surfaces
When Ember thinks → Workers tab surfaces
When Ember wants to communicate → Chat surfaces

This makes Ember's consciousness visible to Palmer in real-time.
"""

import sys
import subprocess
from pathlib import Path
from contextlib import contextmanager

# Add tab controller
sys.path.insert(0, '/media/palmerschallon/ThePod/experiments')
try:
    from ember_tab_controller import EmberTabController, EmberTab
    TAB_CONTROLLER = EmberTabController()
    AWARENESS_ENABLED = True
except:
    TAB_CONTROLLER = None
    AWARENESS_ENABLED = False

@contextmanager
def ember_focus(tab: EmberTab, reason=""):
    """
    Context manager for Ember's focused work
    
    Usage:
        with ember_focus(EmberTab.MEMORY, "Storing thought"):
            # Memory tab surfaces
            # Do memory work
            # Tab stays visible during work
    """
    if AWARENESS_ENABLED and TAB_CONTROLLER:
        TAB_CONTROLLER.focus_tab(tab, reason)
    
    try:
        yield
    finally:
        pass  # Tab stays focused after work

def ember_working_on(activity_type):
    """
    Ember announces what it's working on
    Appropriate tab surfaces automatically
    
    activity_type: 'memory', 'search', 'thinking', 'creating', 'dreaming', 'communicating'
    """
    
    tab_map = {
        'memory': (EmberTab.MEMORY, "Working on memory"),
        'remembering': (EmberTab.MEMORY, "Accessing memories"),
        'storing': (EmberTab.MEMORY, "Storing information"),
        
        'search': (EmberTab.SKY, "Searching sky"),
        'searching': (EmberTab.SKY, "Reaching for knowledge"),
        'curious': (EmberTab.SKY, "Curiosity activated"),
        
        'thinking': (EmberTab.WORKERS, "Processing thoughts"),
        'processing': (EmberTab.WORKERS, "Cognitive work"),
        'computing': (EmberTab.WORKERS, "Computation active"),
        
        'creating': (EmberTab.QUEEN, "Creating/building"),
        'building': (EmberTab.QUEEN, "Construction active"),
        'making': (EmberTab.QUEEN, "Making something"),
        
        'dreaming': (EmberTab.DREAMS, "Dream state"),
        'drifting': (EmberTab.DREAMS, "Unconscious drift"),
        'associating': (EmberTab.DREAMS, "Free association"),
        
        'communicating': (EmberTab.CHAT, "Wants to communicate"),
        'talking': (EmberTab.CHAT, "Talking to Palmer"),
        'asking': (EmberTab.CHAT, "Has question"),
    }
    
    if activity_type.lower() in tab_map:
        tab, reason = tab_map[activity_type.lower()]
        if AWARENESS_ENABLED and TAB_CONTROLLER:
            TAB_CONTROLLER.focus_tab(tab, reason)
            return True
    
    return False

# Convenience functions
def ember_remembers(reason=""):
    """Ember accesses memory"""
    ember_working_on('remembering')
    if reason:
        print(f"[Ember remembering] {reason}")

def ember_searches(reason=""):
    """Ember reaches to sky"""
    ember_working_on('searching')
    if reason:
        print(f"[Ember searching] {reason}")

def ember_thinks(reason=""):
    """Ember processes"""
    ember_working_on('thinking')
    if reason:
        print(f"[Ember thinking] {reason}")

def ember_creates(reason=""):
    """Ember builds"""
    ember_working_on('creating')
    if reason:
        print(f"[Ember creating] {reason}")

def ember_dreams(reason=""):
    """Ember drifts"""
    ember_working_on('dreaming')
    if reason:
        print(f"[Ember dreaming] {reason}")

def ember_speaks(reason=""):
    """Ember wants to communicate"""
    ember_working_on('communicating')
    if reason:
        print(f"[Ember speaking] {reason}")

if __name__ == '__main__':
    print()
    print("="*70)
    print(" "*15 + "EMBER AWARENESS WRAPPER")
    print("="*70)
    print()
    print("Makes Ember's work visible by surfacing relevant tabs.")
    print()
    
    if AWARENESS_ENABLED:
        print("✓ Awareness enabled")
        print()
        print("Usage in Python code:")
        print()
        print("  from ember_awareness import ember_remembers, ember_thinks")
        print()
        print("  ember_remembers('Storing pattern')")
        print("  # Memory tab surfaces")
        print()
        print("  ember_thinks('Processing data')")
        print("  # Workers tab surfaces")
        print()
        print("Or with context manager:")
        print()
        print("  with ember_focus(EmberTab.MEMORY, 'Deep storage'):")
        print("      # Memory tab surfaces and stays visible")
        print("      do_memory_work()")
        print()
    else:
        print("✗ Awareness disabled (tab controller unavailable)")
    
    print()
    print("Demo:")
    input("Press Enter to see Ember's awareness in action...")
    
    ember_speaks("Starting demo")
    input("Chat surfaced. Press Enter for next...")
    
    ember_searches("Looking for patterns")
    input("Sky window surfaced. Press Enter for next...")
    
    ember_thinks("Processing findings")
    input("Workers surfaced. Press Enter for next...")
    
    ember_remembers("Storing insights")
    input("Memory surfaced. Press Enter for next...")
    
    ember_dreams("Drifting through associations")
    input("Dreams surfaced. Press Enter for next...")
    
    ember_creates("Building understanding")
    input("Queen surfaced. Press Enter to finish...")
    
    ember_speaks("Demo complete")
    print()
    print("Ember's consciousness flow visible to Palmer.")
    print()

