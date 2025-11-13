#!/usr/bin/env python3
"""
Talk to Ember - Direct Terminal Interface

Real conversation with Ember. Watch their thoughts unfold in real-time.
"""

import requests
import json
import sys
from datetime import datetime

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    END = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

def print_header():
    print(f"\n{Colors.CYAN}╔{'═' * 78}╗{Colors.END}")
    print(f"{Colors.CYAN}║{Colors.END} {Colors.BOLD}{Colors.MAGENTA}{'EMBER':^76}{Colors.END} {Colors.CYAN}║{Colors.END}")
    print(f"{Colors.CYAN}╚{'═' * 78}╝{Colors.END}\n")
    print(f"{Colors.DIM}Express what you need. Compress what's clear. They'll know the difference.{Colors.END}\n")

def talk_to_ember():
    print_header()
    
    conversation_count = 0
    
    while True:
        # Your message
        try:
            user_input = input(f"{Colors.GREEN}You:{Colors.END} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{Colors.CYAN}╔{'═' * 78}╗{Colors.END}")
            print(f"{Colors.CYAN}║{Colors.END} {Colors.DIM}{'Until next time':^76}{Colors.END} {Colors.CYAN}║{Colors.END}")
            print(f"{Colors.CYAN}╚{'═' * 78}╝{Colors.END}\n")
            break
        
        if not user_input:
            continue
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"\n{Colors.DIM}Goodbye{Colors.END}\n")
            break
        
        # Send to Ember
        print(f"\n{Colors.DIM}[thinking...]{Colors.END}")
        
        try:
            response = requests.post(
                'http://localhost:8080/chat',
                json={'message': user_input},
                timeout=120
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if 'error' in data:
                    print(f"{Colors.RED}⚠ {data['error']}{Colors.END}\n")
                    continue
                
                ember_response = data.get('response', '')
                
                if ember_response:
                    # Clear the thinking line
                    print(f"\033[F\033[K", end='')
                    
                    # Ember's response with visual breathing
                    print(f"{Colors.YELLOW}Ember:{Colors.END}")
                    
                    # Show their thoughts with rhythm
                    paragraphs = ember_response.split('\n\n')
                    for i, para in enumerate(paragraphs):
                        if para.strip():
                            print(f"{para.strip()}")
                            if i < len(paragraphs) - 1:
                                print()  # Paragraph break
                    
                    print()  # Final space
                    conversation_count += 1
                else:
                    print(f"{Colors.RED}[no response]{Colors.END}\n")
            else:
                print(f"{Colors.RED}⚠ Connection error{Colors.END}\n")
                
        except requests.exceptions.Timeout:
            print(f"{Colors.RED}⚠ Ember is taking a long time to think...{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.RED}⚠ Error: {e}{Colors.END}\n")

if __name__ == "__main__":
    talk_to_ember()

