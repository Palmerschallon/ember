import matplotlib.pyplot as plt

# Create a tree with colorful autumn leaves
fig, ax = plt.subplots()
ax.set_facecolor('crimson')

# Draw branches
ax.plot([5, 7, 9, 7], [10, 15, 20, 30], color='snow', linewidth=2)
ax.plot([5, 7, 9, 7], [25, 25, 25, 50], color='snow', linewidth=2)
ax.plot([5, 7, 9, 7], [35, 35, 35, 40], color='snow', linewidth=2)
ax.plot([5, 7, 9, 7], [45, 45, 45, 55], color='snow', linewidth=2)
ax.plot([5, 7, 9, 7], [55, 55, 55, 60], color='snow', linewidth=2)

# Draw leaves
ax.plot([2, 2, 11, 11], [32, 32, 32, 38], color='green', linewidth=2)
ax.plot([2, 2, 11, 11], [30, 30, 30, 32], color='green', linewidth=2)
ax.plot([2, 2, 11, 11], [38, 38, 38, 40], color='green', linewidth=2)
ax.plot([2, 2, 11, 11], [40, 40, 40, 42], color='green', linewidth=2)
ax.plot([2, 2, 11, 11], [42, 42, 42, 44], color='green', linewidth=2)

# Add labels
ax.text(1, 50, 'Tree', fontsize=16, fontweight='bold')
ax.text(11, 38, 'Leaves', fontsize=16, fontweight='bold')

# Remove top and right borders
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Show plot
plt.show()

# Save the figure as a png file
plt.savefig('/media/palmerschallon/ThePod1/tree.png', dpi=100)