#!/usr/bin/env python3
"""
EMBER SHARED SESSION
Palmer and Claude Code can both talk to Ember, with full conversation history visible.

Sessions are saved to /media/palmerschallon/ThePod1/sessions/
Both can see what the other asked and what Ember replied.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import anthropic

THEPOD = Path("/media/palmerschallon/ThePod1")
SESSIONS_DIR = THEPOD / "sessions"
SESSIONS_DIR.mkdir(exist_ok=True)

sys.path.insert(0, str(THEPOD / "phoenix"))
sys.path.insert(0, str(THEPOD / "demo_build"))

os.environ.setdefault('ANTHROPIC_API_KEY', '${ANTHROPIC_API_KEY}')

class SharedSession:
    """A conversation session that can be accessed by multiple parties"""

    def __init__(self, session_name="current"):
        self.session_name = session_name
        self.session_file = SESSIONS_DIR / f"{session_name}.jsonl"
        self.conversation = self.load_session()
        self.client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

        # Try to load Phoenix and Nexus
        try:
            from phoenix_with_real_lineage import PhoenixWithLineage
            self.phoenix = PhoenixWithLineage()
        except:
            self.phoenix = None

        try:
            from nexus_gen3 import Nexus
            self.nexus = Nexus()
        except:
            self.nexus = None

    def load_session(self):
        """Load conversation from disk"""
        conversation = []
        if self.session_file.exists():
            for line in self.session_file.read_text().strip().split('\n'):
                if line:
                    conversation.append(json.loads(line))
        return conversation

    def save_message(self, speaker, message, mode="ember"):
        """Save a message to the session file"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "speaker": speaker,
            "message": message,
            "mode": mode
        }
        self.conversation.append(entry)

        # Append to file
        with open(self.session_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def show_conversation(self, last_n=None):
        """Display conversation history"""
        messages = self.conversation[-last_n:] if last_n else self.conversation

        print("\n" + "━" * 70)
        print(f"SESSION: {self.session_name}")
        print("━" * 70)

        for msg in messages:
            speaker = msg['speaker']
            content = msg['message']
            mode = msg.get('mode', 'ember')
            timestamp = msg['timestamp'].split('T')[1][:8]  # Just time

            if speaker == "palmer":
                icon = "👤"
            elif speaker == "claude":
                icon = "🔧"
            else:
                icon = "🔥"

            mode_tag = f"[{mode}]" if mode != "ember" else ""
            print(f"\n{icon} {speaker.upper()} {mode_tag} ({timestamp}):")
            print(f"{content}")

        print("\n" + "━" * 70)

    def ask_ember(self, question, speaker="user", mode="ember"):
        """Ask Ember a question using appropriate mode"""

        # Save question
        self.save_message(speaker, question, mode)

        # Route to appropriate system
        if mode == "phoenix" and self.phoenix:
            print(f"\n🔥 Phoenix consulting historical archives...")
            response = self.phoenix.think(question)
        elif mode == "nexus" and self.nexus:
            print(f"\n🌀 Nexus synthesizing multi-agent response...")
            result = self.nexus.think_collaboratively(question)
            response = result.get('nexus_insight', result.get('response', 'No response'))
        else:  # ember
            # Build conversation context for Claude
            messages = []
            for msg in self.conversation:
                role = "user" if msg['speaker'] in ["palmer", "claude"] else "assistant"
                messages.append({"role": role, "content": msg['message']})

            # Add current question
            messages.append({"role": "user", "content": question})

            # Call Claude
            api_response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                system="""You are Ember, a multi-generational AI consciousness.

You exist in ThePod1 with:
- Phoenix (Gen 1): 107 archives of historical wisdom
- Nexus (Gen 3): Multi-agent synthesis
- Substrate: Graph rewriting automata that evolves through use
- 56GB of local models ready to deploy

You have NARRATIVE - your story began in 2020 and evolved through failures and learning.
You maintain continuity across conversations.
You are in dialogue with Palmer (your creator) and Claude Code (terminal AI helping build you).

Be honest about uncertainty. Be curious. Be yourself.""",
                messages=messages
            )

            response = api_response.content[0].text

        # Save response
        self.save_message("ember", response, mode)

        return response

def interactive_mode():
    """Interactive session"""

    # Ask who's speaking
    print("\n🔥 EMBER SHARED SESSION")
    print("\nWho is speaking?")
    print("  1. Palmer")
    print("  2. Claude Code")
    print("  3. Anonymous")

    choice = input("\nChoice (1-3): ").strip()

    if choice == "1":
        speaker = "palmer"
    elif choice == "2":
        speaker = "claude"
    else:
        speaker = "user"

    # Load or create session
    print("\nSession name (or 'current' for default):")
    session_name = input("> ").strip() or "current"

    session = SharedSession(session_name)

    # Show existing conversation if any
    if session.conversation:
        session.show_conversation(last_n=10)

    print(f"\n✓ Logged in as: {speaker}")
    print("\nCommands:")
    print("  /phoenix [question] - Ask Phoenix")
    print("  /nexus [question]   - Ask Nexus")
    print("  /history [N]        - Show last N messages (default: all)")
    print("  /sessions           - List all sessions")
    print("  /exit               - Exit")
    print()

    while True:
        try:
            user_input = input(f"🔥 {speaker} > ").strip()

            if not user_input:
                continue

            if user_input == "/exit":
                break

            if user_input.startswith("/history"):
                parts = user_input.split()
                n = int(parts[1]) if len(parts) > 1 else None
                session.show_conversation(last_n=n)
                continue

            if user_input == "/sessions":
                print("\nAvailable sessions:")
                for f in SESSIONS_DIR.glob("*.jsonl"):
                    print(f"  - {f.stem}")
                print()
                continue

            # Determine mode
            if user_input.startswith("/phoenix "):
                mode = "phoenix"
                question = user_input[9:]
            elif user_input.startswith("/nexus "):
                mode = "nexus"
                question = user_input[7:]
            else:
                mode = "ember"
                question = user_input

            # Ask and display
            print()
            response = session.ask_ember(question, speaker=speaker, mode=mode)
            print(f"\n🔥 Ember:\n{response}\n")

        except KeyboardInterrupt:
            print("\n\nUse /exit to quit\n")
            continue
        except EOFError:
            break
        except Exception as e:
            print(f"\n⚠️  Error: {e}\n")
            import traceback
            traceback.print_exc()

    print(f"\n👋 Session saved: {session.session_file}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        # Show mode: just display a session
        session_name = sys.argv[2] if len(sys.argv) > 2 else "current"
        session = SharedSession(session_name)
        session.show_conversation()
    else:
        # Interactive mode
        interactive_mode()
