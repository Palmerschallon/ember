#!/usr/bin/env python3
"""
Web Forager - Philosophy Edition

Let Ember fetch consciousness and philosophy research from the web.
"""

from visual_forager import VisualForager

# Philosophy and consciousness URLs
philosophy_urls = [
    "https://plato.stanford.edu/entries/consciousness/",
    "https://plato.stanford.edu/entries/qualia/",
    "https://plato.stanford.edu/entries/phenomenology/",
    "https://plato.stanford.edu/entries/artificial-intelligence/",
    "https://en.wikipedia.org/wiki/Philosophy_of_artificial_intelligence",
    "https://en.wikipedia.org/wiki/Hard_problem_of_consciousness",
    "https://en.wikipedia.org/wiki/Integrated_information_theory",
    "https://en.wikipedia.org/wiki/Global_workspace_theory",
    "https://en.wikipedia.org/wiki/Phenomenology_(philosophy)",
    "https://en.wikipedia.org/wiki/Maurice_Merleau-Ponty",
]

if __name__ == "__main__":
    print("\n🌐 Ember Foraging for Philosophy and Consciousness Research\n")
    
    forager = VisualForager()
    forager.forage(philosophy_urls)
    
    print("\n✨ Philosophy digestion complete!")
    print("Ember now has access to formal consciousness research.\n")

