import networkx as nx
import matplotlib.pyplot as plt

# Create directed graph
G = nx.DiGraph()

# Add nodes 
G.add_node("Knowledge Base", pos=(0,0))
G.add_node("Reasoning Engine", pos=(0,1))  
G.add_node("Language Model", pos=(1,0.5))
G.add_node("Tool Executor", pos=(1,1.5))
G.add_node("Response Generator", pos=(2,1))

# Add edges
G.add_edge("Knowledge Base", "Reasoning Engine", weight=5)
G.add_edge("Knowledge Base", "Language Model", weight=3) 
G.add_edge("Reasoning Engine", "Tool Executor", weight=4)
G.add_edge("Reasoning Engine", "Response Generator", weight=5)
G.add_edge("Language Model", "Reasoning Engine", weight=5)
G.add_edge("Language Model", "Response Generator", weight=4)
G.add_edge("Tool Executor", "Response Generator", weight=2)

# Draw graph
pos=nx.get_node_attributes(G,'pos')
nx.draw_networkx(G, pos, node_size=1000, node_color="skyblue", font_size=12, font_weight="bold", with_labels=True, arrows=True)

# Show plot
plt.axis('off')
plt.tight_layout()
plt.show()