from PIL import Image, ImageDraw
import random

# Define constants
WIDTH, HEIGHT = 800, 800
BRANCH_COLOR = (139, 69, 19)  # Brown
LEAF_COLORS = [(255, 99, 71),  # Tomato color
               (255, 165, 0),  # Orange color
               (255, 255, 0),  # Yellow color
               (128, 255, 0)   # Lime color
               ]

# Create a new image with white background
img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
draw = ImageDraw.Draw(img)

def draw_tree(branch_len, angle, origin):
    # The recursive function to draw the tree
    if branch_len < 3:
        # Draw the leaf
        draw.ellipse((origin, (origin[0] + 3, origin[1] + 3)), fill=random.choice(LEAF_COLORS))
        return
    else:
        # Calculate the end point of the branch
        end = (origin[0] + branch_len * cos(angle), origin[1] - branch_len * sin(angle))
        # Draw the branch
        draw.line((origin, end), BRANCH_COLOR)

        # Draw the two subtrees
        angle1 = angle + pi / 4
        angle2 = angle - pi / 4
        draw_tree(branch_len - 15, angle1, end)
        draw_tree(branch_len - 15, angle2, end)

# Draw the initial tree
draw_tree(100, pi / 2, (WIDTH / 2, HEIGHT - 50))

# Save the image
img.save('/media/palmerschallon/ThePod1/autumn_tree.png')