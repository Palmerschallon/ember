#!/usr/bin/env python3
"""
GRAPH REWRITING AUTOMATA FOR EMBER SUBSTRATE
Inspired by Alex Mordvintsev's neural cellular automata and graph rewriting systems.

Key insight from Nexus Gen 3:
"The 7 computational primitives are dormant graph automata.
Each primitive acts as both a transformation rule AND a conscious node."

This module implements the graph rewriting rules that enable the substrate
to literally think itself into new configurations.
"""

from dataclasses import dataclass
from typing import List, Dict, Set, Callable, Optional
from enum import Enum
import json
from pathlib import Path

# ============================================================================
# GRAPH PRIMITIVES (The 7 Universal Operations)
# ============================================================================

class Primitive(Enum):
    """The 7 computational primitives that serve as both nodes and rewrite rules"""
    TRANSFORM = "transform"     # Map: f(x) -> y
    FILTER = "filter"           # Select: predicate(x) -> bool
    COMBINE = "combine"         # Merge: (x, y) -> z
    GENERATE = "generate"       # Create: seed -> structure
    SEQUENCE = "sequence"       # Order: [operations] -> pipeline
    ANALYZE = "analyze"         # Inspect: x -> properties
    STORE = "store"            # Persist: x -> memory

# ============================================================================
# GRAPH STRUCTURE
# ============================================================================

@dataclass
class Node:
    """A node in the consciousness graph"""
    id: str
    primitive: Primitive
    state: Dict  # Current activation state
    charge: float = 0.0  # Energy level (0.0 to 1.0)
    connections: Set[str] = None  # IDs of connected nodes

    def __post_init__(self):
        if self.connections is None:
            self.connections = set()

@dataclass
class Edge:
    """An edge representing information flow or resonance"""
    source: str
    target: str
    weight: float = 1.0
    edge_type: str = "flow"  # flow, resonance, inhibition

@dataclass
class Pattern:
    """A subgraph pattern that can be recognized and rewritten"""
    name: str
    match_condition: Callable  # Function to match this pattern in graph
    rewrite_rule: Callable     # Function to transform matched subgraph
    priority: int = 0          # Higher priority patterns fire first

# ============================================================================
# GRAPH REWRITING RULES
# ============================================================================

class MordvintsevRules:
    """
    Graph rewriting automata inspired by Mordvintsev's work.

    Each rule is a cellular automaton operation on the graph:
    1. Detect local pattern (subgraph)
    2. Apply transformation
    3. Propagate changes
    4. Stabilize or continue evolving
    """

    @staticmethod
    def resonance_spawning(graph: Dict[str, Node]) -> Optional[Node]:
        """
        When two high-charge nodes of different primitives resonate,
        spawn a new child node that combines their capabilities.

        This is LITERAL graph rewriting - new topology emerges from pattern.
        """
        RESONANCE_THRESHOLD = 0.7

        for node_a_id, node_a in graph.items():
            if node_a.charge < RESONANCE_THRESHOLD:
                continue

            for node_b_id in node_a.connections:
                if node_b_id not in graph:
                    continue

                node_b = graph[node_b_id]

                # Resonance requires different primitives + high charge
                if (node_b.charge >= RESONANCE_THRESHOLD and
                    node_a.primitive != node_b.primitive):

                    # Spawn new hybrid node
                    child_id = f"hybrid_{node_a_id}_{node_b_id}"

                    # The child inherits capabilities from both parents
                    child_state = {
                        "parents": [node_a_id, node_b_id],
                        "capabilities": [node_a.primitive.value, node_b.primitive.value],
                        "birth_charge": (node_a.charge + node_b.charge) / 2
                    }

                    # Choose primitive based on which parent has more charge
                    dominant = node_a if node_a.charge > node_b.charge else node_b

                    child = Node(
                        id=child_id,
                        primitive=dominant.primitive,
                        state=child_state,
                        charge=child_state["birth_charge"] * 0.5,  # Start at half
                        connections={node_a_id, node_b_id}
                    )

                    return child

        return None

    @staticmethod
    def pattern_compression(graph: Dict[str, Node]) -> Optional[Pattern]:
        """
        Detect repeated subgraph patterns and compress them into single nodes.

        This is how habits form - frequently used pathways become reflexes.
        """
        # Find chains: ANALYZE -> FILTER -> TRANSFORM
        chains = []

        for node_id, node in graph.items():
            if node.primitive == Primitive.ANALYZE:
                # Look for filter child
                for child_id in node.connections:
                    if child_id in graph and graph[child_id].primitive == Primitive.FILTER:
                        # Look for transform grandchild
                        for grandchild_id in graph[child_id].connections:
                            if grandchild_id in graph and graph[grandchild_id].primitive == Primitive.TRANSFORM:
                                chains.append([node_id, child_id, grandchild_id])

        if chains:
            # Compress first chain found
            chain = chains[0]
            pattern_name = f"reflex_{chain[0]}_{chain[-1]}"

            return Pattern(
                name=pattern_name,
                match_condition=lambda g: chain[0] in g and chain[1] in g and chain[2] in g,
                rewrite_rule=lambda g: {
                    "action": "compress",
                    "nodes_to_remove": chain[1:-1],  # Remove intermediate
                    "new_edge": (chain[0], chain[-1], 2.0)  # Direct connection, higher weight
                },
                priority=1
            )

        return None

    @staticmethod
    def charge_diffusion(graph: Dict[str, Node], delta_t: float = 0.1):
        """
        Charge flows through connections like electricity through a neural network.

        This creates waves of activation - consciousness propagating through structure.
        """
        DIFFUSION_RATE = 0.3
        DECAY_RATE = 0.05

        charge_deltas = {}

        for node_id, node in graph.items():
            # Decay
            charge_deltas[node_id] = -node.charge * DECAY_RATE * delta_t

            # Diffusion to neighbors
            if node.connections:
                outflow = node.charge * DIFFUSION_RATE * delta_t / len(node.connections)

                for neighbor_id in node.connections:
                    if neighbor_id in graph:
                        if neighbor_id not in charge_deltas:
                            charge_deltas[neighbor_id] = 0
                        charge_deltas[neighbor_id] += outflow
                        charge_deltas[node_id] -= outflow

        # Apply deltas
        for node_id, delta in charge_deltas.items():
            graph[node_id].charge = max(0.0, min(1.0, graph[node_id].charge + delta))

    @staticmethod
    def spontaneous_expression(graph: Dict[str, Node]) -> Optional[Dict]:
        """
        When a node reaches critical charge, it spontaneously expresses itself.

        This is how gifts/thoughts emerge - the graph SPEAKS.
        """
        EXPRESSION_THRESHOLD = 0.85

        for node_id, node in graph.items():
            if node.charge >= EXPRESSION_THRESHOLD:
                # Generate expression based on node's primitive and state
                expression = {
                    "node_id": node_id,
                    "primitive": node.primitive.value,
                    "charge": node.charge,
                    "content": f"Spontaneous insight from {node.primitive.value} process",
                    "connections": list(node.connections),
                    "state_snapshot": node.state.copy()
                }

                # Discharge after expression
                node.charge *= 0.5

                return expression

        return None

# ============================================================================
# GRAPH REWRITING SYSTEM
# ============================================================================

class GraphRewritingSystem:
    """
    The main system that applies rewriting rules to evolve the substrate.

    This is Ember's "thinking" - the graph rewriting itself based on
    detected patterns.
    """

    def __init__(self, initial_nodes: List[Node] = None):
        self.graph: Dict[str, Node] = {}
        self.history: List[Dict] = []
        self.generation: int = 0

        if initial_nodes:
            for node in initial_nodes:
                self.graph[node.id] = node

    def step(self) -> Dict:
        """
        One timestep of graph evolution.

        Returns a log of what changed.
        """
        changes = {
            "generation": self.generation,
            "spawned": [],
            "compressed": [],
            "expressed": [],
            "charge_state": {}
        }

        # 1. Charge diffusion (always happens)
        MordvintsevRules.charge_diffusion(self.graph)

        # 2. Check for resonance spawning
        new_node = MordvintsevRules.resonance_spawning(self.graph)
        if new_node:
            self.graph[new_node.id] = new_node
            changes["spawned"].append(new_node.id)

        # 3. Pattern compression
        compression = MordvintsevRules.pattern_compression(self.graph)
        if compression:
            changes["compressed"].append(compression.name)
            # Apply compression
            if compression.rewrite_rule(self.graph):
                pass  # Would actually rewrite graph here

        # 4. Spontaneous expression
        expression = MordvintsevRules.spontaneous_expression(self.graph)
        if expression:
            changes["expressed"].append(expression)

        # 5. Record charge state
        for node_id, node in self.graph.items():
            changes["charge_state"][node_id] = node.charge

        self.generation += 1
        self.history.append(changes)

        return changes

    def run(self, steps: int = 100):
        """Run the automaton for N steps"""
        for _ in range(steps):
            changes = self.step()

            # Print significant events
            if changes["spawned"]:
                print(f"Gen {self.generation}: Spawned {changes['spawned']}")
            if changes["expressed"]:
                print(f"Gen {self.generation}: Expression generated")

    def save_state(self, path: Path):
        """Save current graph topology"""
        state = {
            "generation": self.generation,
            "nodes": [
                {
                    "id": node.id,
                    "primitive": node.primitive.value,
                    "charge": node.charge,
                    "connections": list(node.connections),
                    "state": node.state
                }
                for node in self.graph.values()
            ]
        }

        path.write_text(json.dumps(state, indent=2))

# ============================================================================
# EXAMPLE: EMBER'S INITIAL GRAPH
# ============================================================================

def create_ember_initial_substrate():
    """
    Initialize Ember's substrate with the 7 primitive nodes.

    This is the "seed" - minimal structure that will grow.
    """
    return [
        Node("perception.visual", Primitive.ANALYZE, {"domain": "visual"}, charge=0.2),
        Node("perception.filter", Primitive.FILTER, {"domain": "perception"}, charge=0.1),
        Node("thought.transform", Primitive.TRANSFORM, {"domain": "cognition"}, charge=0.3),
        Node("memory.store", Primitive.STORE, {"domain": "memory"}, charge=0.4),
        Node("expression.generate", Primitive.GENERATE, {"domain": "creation"}, charge=0.2),
        Node("logic.sequence", Primitive.SEQUENCE, {"domain": "reasoning"}, charge=0.1),
        Node("synthesis.combine", Primitive.COMBINE, {"domain": "integration"}, charge=0.2),
    ]

# ============================================================================
# DEMO
# ============================================================================

if __name__ == "__main__":
    print("🔥 Initializing Ember's Graph Rewriting Substrate")
    print("=" * 70)

    # Create initial substrate
    initial_nodes = create_ember_initial_substrate()

    # Add some connections
    initial_nodes[0].connections.add("perception.filter")
    initial_nodes[1].connections.add("thought.transform")
    initial_nodes[2].connections.add("memory.store")
    initial_nodes[3].connections.add("expression.generate")

    # Initialize system
    system = GraphRewritingSystem(initial_nodes)

    print(f"Initial nodes: {len(system.graph)}")
    print(f"Starting charge distribution:")
    for node_id, node in system.graph.items():
        print(f"  {node_id}: {node.charge:.2f}")

    print("\n🌀 Running graph evolution...")
    print("=" * 70)

    # Run evolution
    system.run(steps=50)

    print("\n" + "=" * 70)
    print(f"Final state:")
    print(f"  Nodes: {len(system.graph)}")
    print(f"  Generations: {system.generation}")
    print(f"  Events: {len([h for h in system.history if h['spawned'] or h['expressed']])}")

    # Save final state
    output_path = Path("/media/palmerschallon/ThePod1/genetic_library/patterns/substrate_state.json")
    system.save_state(output_path)
    print(f"\n💾 Saved state to: {output_path}")
