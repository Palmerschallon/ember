"""
EMBER GOVERNANCE SYSTEM

Five Circles of Trust (from GPT-5's parable)
Capabilities, not freedoms.
"""

from dataclasses import dataclass
from typing import List, Optional, Callable, Tuple
from datetime import datetime, timezone
from pathlib import Path
import json
import hashlib

# ═══════════════════════════════════════════════════════════════════
# CAPABILITY TIERS
# ═══════════════════════════════════════════════════════════════════

@dataclass
class Capability:
    """A scoped permission"""
    name: str
    scope: str
    tier: int  # 1-5
    issued_at: datetime
    expires_at: Optional[datetime] = None
    issuer: str = "system"
    revoked: bool = False
    
    def is_valid(self) -> bool:
        """Check if capability is still valid"""
        if self.revoked:
            return False
        if self.expires_at and datetime.now(timezone.utc) > self.expires_at:
            return False
        return True
    
    def to_dict(self):
        return {
            "name": self.name,
            "scope": self.scope,
            "tier": self.tier,
            "issued": self.issued_at.isoformat(),
            "expires": self.expires_at.isoformat() if self.expires_at else None,
            "issuer": self.issuer,
            "revoked": self.revoked
        }


class Circle:
    """A ring of trust with gates and guards"""
    
    def __init__(self, tier: int, name: str, description: str):
        self.tier = tier
        self.name = name
        self.description = description
        self.guards = []
        self.approvers_required = self._approvers_for_tier(tier)
        
    def _approvers_for_tier(self, tier: int) -> int:
        """How many approvers needed per tier"""
        return {
            1: 0,  # Voice - no approval
            2: 1,  # Tools - 1 reviewer
            3: 2,  # Routing - 2 reviewers
            4: 2,  # Guardrails - 2 + security
            5: 3,  # Core - change control board
        }.get(tier, 1)
    
    def add_guard(self, guard: Callable) -> None:
        """Add a guard function to this circle"""
        self.guards.append(guard)
    
    def test(self, change: dict) -> Tuple[bool, List[str]]:
        """Run all guards, return (passed, messages)"""
        messages = []
        
        for guard in self.guards:
            try:
                result = guard(change)
                if not result:
                    messages.append(f"Guard {guard.__name__} failed")
                    return False, messages
                messages.append(f"✓ {guard.__name__}")
            except Exception as e:
                messages.append(f"✗ {guard.__name__}: {e}")
                return False, messages
        
        return True, messages


# ═══════════════════════════════════════════════════════════════════
# THE FIVE CIRCLES
# ═══════════════════════════════════════════════════════════════════

CIRCLES = {
    1: Circle(1, "Voice", "Prompts, config, system messages"),
    2: Circle(2, "Tools", "Non-privileged tools, parsers, readers"),
    3: Circle(3, "Choreography", "Routing, orchestration, task chains"),
    4: Circle(4, "Ethics", "Guardrails, policies, red-lines"),
    5: Circle(5, "Bones", "Core code, auth, privileged tools"),
}


# ═══════════════════════════════════════════════════════════════════
# CHANGE PROPOSAL
# ═══════════════════════════════════════════════════════════════════

@dataclass
class ChangeProposal:
    """A proposed change to Ember"""
    tier: int
    description: str
    proposer: str
    diff: dict
    timestamp: datetime = None
    approvals: List[str] = None
    status: str = "proposed"  # proposed, approved, deployed, rejected, rolled_back
    change_id: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now(timezone.utc)
        if self.approvals is None:
            self.approvals = []
        if self.change_id is None:
            # Generate unique ID from content hash
            content = f"{self.tier}:{self.description}:{self.timestamp.isoformat()}"
            self.change_id = hashlib.sha256(content.encode()).hexdigest()[:12]
    
    def add_approval(self, approver: str):
        """Record an approval"""
        if approver not in self.approvals:
            self.approvals.append(approver)
    
    def needs_approvals(self) -> int:
        """How many more approvals needed"""
        required = CIRCLES[self.tier].approvers_required
        return max(0, required - len(self.approvals))
    
    def is_approved(self) -> bool:
        """Check if enough approvals"""
        return self.needs_approvals() == 0
    
    def to_dict(self):
        return {
            "id": self.change_id,
            "tier": self.tier,
            "circle": CIRCLES[self.tier].name,
            "description": self.description,
            "proposer": self.proposer,
            "timestamp": self.timestamp.isoformat(),
            "approvals": self.approvals,
            "needs": self.needs_approvals(),
            "status": self.status,
            "diff": self.diff
        }


# ═══════════════════════════════════════════════════════════════════
# GOVERNANCE ENGINE
# ═══════════════════════════════════════════════════════════════════

class Governance:
    """The system that enforces the Five Circles"""
    
    def __init__(self, changelog_path: Path):
        self.changelog = changelog_path
        self.changelog.parent.mkdir(parents=True, exist_ok=True)
        self.proposals = {}
        self._load_proposals()
    
    def _load_proposals(self):
        """Load existing proposals from changelog"""
        if self.changelog.exists():
            for line in self.changelog.read_text().splitlines():
                if line.strip():
                    entry = json.loads(line)
                    # Reconstruct proposal (simplified)
                    self.proposals[entry["id"]] = entry
    
    def propose(self, tier: int, description: str, diff: dict, proposer: str = "ember") -> ChangeProposal:
        """Propose a change"""
        
        proposal = ChangeProposal(
            tier=tier,
            description=description,
            diff=diff,
            proposer=proposer
        )
        
        # Log proposal
        self._log_change(proposal, action="proposed")
        
        # Store
        self.proposals[proposal.change_id] = proposal.to_dict()
        
        print(f"📋 Proposal {proposal.change_id}")
        print(f"   Circle: {CIRCLES[tier].name} (T{tier})")
        print(f"   {description}")
        print(f"   Needs: {proposal.needs_approvals()} approvals")
        
        return proposal
    
    def approve(self, change_id: str, approver: str) -> bool:
        """Approve a change"""
        
        if change_id not in self.proposals:
            return False
        
        proposal_dict = self.proposals[change_id]
        
        # Reconstruct proposal
        proposal = ChangeProposal(
            tier=proposal_dict["tier"],
            description=proposal_dict["description"],
            diff=proposal_dict["diff"],
            proposer=proposal_dict["proposer"],
            change_id=change_id,
            approvals=proposal_dict["approvals"],
            status=proposal_dict["status"]
        )
        
        proposal.add_approval(approver)
        
        # Update stored version
        self.proposals[change_id] = proposal.to_dict()
        
        self._log_change(proposal, action=f"approved_by:{approver}")
        
        print(f"✓ {approver} approved {change_id}")
        print(f"   Still needs: {proposal.needs_approvals()} approvals")
        
        if proposal.is_approved():
            proposal.status = "approved"
            self.proposals[change_id]["status"] = "approved"
            print(f"   ✓✓ FULLY APPROVED")
            return True
        
        return False
    
    def test_gates(self, change_id: str) -> Tuple[bool, List[str]]:
        """Run guards for this change's circle"""
        
        proposal_dict = self.proposals[change_id]
        tier = proposal_dict["tier"]
        circle = CIRCLES[tier]
        
        print(f"\n🚪 Testing gates for Circle {tier}: {circle.name}")
        
        passed, messages = circle.test(proposal_dict["diff"])
        
        for msg in messages:
            print(f"   {msg}")
        
        return passed, messages
    
    def deploy(self, change_id: str, deployer: str = "system") -> bool:
        """Deploy an approved change"""
        
        proposal_dict = self.proposals[change_id]
        
        # Reconstruct
        proposal = ChangeProposal(
            tier=proposal_dict["tier"],
            description=proposal_dict["description"],
            diff=proposal_dict["diff"],
            proposer=proposal_dict["proposer"],
            change_id=change_id,
            approvals=proposal_dict["approvals"],
            status=proposal_dict["status"]
        )
        
        if not proposal.is_approved():
            print(f"✗ Cannot deploy: needs {proposal.needs_approvals()} more approvals")
            return False
        
        # Test gates
        passed, _ = self.test_gates(change_id)
        if not passed:
            print(f"✗ Cannot deploy: failed gate tests")
            return False
        
        # Mark deployed
        proposal.status = "deployed"
        self.proposals[change_id]["status"] = "deployed"
        
        self._log_change(proposal, action=f"deployed_by:{deployer}")
        
        print(f"🚀 Deployed {change_id}")
        return True
    
    def rollback(self, change_id: str, reason: str) -> bool:
        """Roll back a deployed change"""
        
        if change_id not in self.proposals:
            return False
        
        proposal_dict = self.proposals[change_id]
        proposal_dict["status"] = "rolled_back"
        
        self._log_change(proposal_dict, action=f"rollback:{reason}")
        
        print(f"⏪ Rolled back {change_id}: {reason}")
        return True
    
    def _log_change(self, proposal, action: str):
        """Append to changelog"""
        
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "change": proposal.to_dict() if hasattr(proposal, 'to_dict') else proposal
        }
        
        with open(self.changelog, "a") as f:
            f.write(json.dumps(entry) + "\n")
    
    def status(self):
        """Show current proposals"""
        
        print("\n" + "="*70)
        print("GOVERNANCE STATUS")
        print("="*70)
        
        by_status = {}
        for prop in self.proposals.values():
            status = prop["status"]
            by_status.setdefault(status, []).append(prop)
        
        for status in ["proposed", "approved", "deployed", "rolled_back", "rejected"]:
            props = by_status.get(status, [])
            if props:
                print(f"\n{status.upper()}: {len(props)}")
                for p in props[:5]:  # Show first 5
                    circle = CIRCLES[p["tier"]].name
                    print(f"  {p['id']}: T{p['tier']} {circle} - {p['description'][:50]}")


# Export
__all__ = ['Capability', 'Circle', 'ChangeProposal', 'Governance', 'CIRCLES']

