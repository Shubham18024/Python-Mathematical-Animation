import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


LADDER_LENGTH = 4.0
FRAMES = 200          # Slightly fewer frames for quicker processing
INTERVAL = 15         # Lower number = Faster Animation (15ms per frame)
FPS = 60              


fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.5, LADDER_LENGTH + 0.5)
ax.set_ylim(-0.5, LADDER_LENGTH + 0.5)

# Static Environment (Wall and Floor)
ax.axhline(0, color='black', linewidth=3)
ax.axvline(0, color='black', linewidth=3)
ax.set_aspect('equal') # Crucial for accurate geometry

# --- Initialize Elements ---
ladder_line, = ax.plot([], [], 'brown', linewidth=4, label='Ladder')
trace_line, = ax.plot([], [], 'b--', linewidth=1, alpha=0.5, label='Path')
cat_body, = ax.plot([], [], 'o', color='orange', markersize=15, markeredgecolor='black')
cat_text = ax.text(0, 0, '', fontsize=12, ha='center', va='center')

# Storage for the path trace
path_x, path_y = [], []

# --- Math & Logic ---
# We animate the angle changing from 90 degrees (vertical) down to 0 (flat)
angles = np.linspace(np.pi/2, 0, FRAMES)

def init():
    """Reset the animation."""
    ladder_line.set_data([], [])
    trace_line.set_data([], [])
    cat_body.set_data([], [])
    cat_text.set_text('')
    path_x.clear()
    path_y.clear()
    return ladder_line, trace_line, cat_body, cat_text

def update(angle):
    """Update positions for a single frame."""
    # 1. Calculate Ladder Ends using Trigonometry
    # Wall (Top): x=0, y varies
    # Floor (Bottom): x varies, y=0
    wall_x, wall_y = 0, LADDER_LENGTH * np.sin(angle)
    floor_x, floor_y = LADDER_LENGTH * np.cos(angle), 0
    
    # Update Ladder Line
    ladder_line.set_data([wall_x, floor_x], [wall_y, floor_y])
    
    # 2. Calculate Cat (Midpoint) Position
    cat_x = (wall_x + floor_x) / 2
    cat_y = (wall_y + floor_y) / 2
    
    # 3. Update Path Trace
    path_x.append(cat_x)
    path_y.append(cat_y)
    trace_line.set_data(path_x, path_y)
    
    # 4. Update Cat Visuals
    cat_body.set_data([cat_x], [cat_y])
    cat_text.set_position((cat_x, cat_y + 0.2)) # Float text slightly above
    cat_text.set_text("🐱")
    
    return ladder_line, trace_line, cat_body, cat_text

# Create Animation
ani = animation.FuncAnimation(
    fig, update, frames=angles, init_func=init, blit=True, interval=INTERVAL
)

plt.title("Cat on Sliding Ladder (Faster)")
plt.grid(True, linestyle=':', alpha=0.6)

# # --- Save the Video ---

# try:
#     print("Saving video... this may take a moment.")
#     ani.save(r"C:\Users\Shubham\Desktop\cat_ladder_fast.mp4", writer='ffmpeg', fps=FPS)
#     print("Video saved as 'cat_ladder_fast.mp4'")
# except Exception as e:
#     print(f"Could not save video: {e}. (Ensure ffmpeg is installed)")

plt.show()
