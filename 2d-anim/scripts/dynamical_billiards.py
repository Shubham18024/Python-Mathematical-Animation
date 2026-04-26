import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

theme = {
    "bg": "#0e1117",          # dark background
    "trajectory": "cyan",
    "points": "red",
    "heatmap": "inferno"
}


# SAFE INPUT

def parse_input(expr):
    try:
        return float(eval(expr, {"__builtins__": None}, {
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e":math.e
        }))
    except:
        return None

# =========================
# ENGINE
# =========================
class Billiard:
    def __init__(self):
        self.set_slope(1)
        self.reset()

    def reset(self):
        self.x, self.y = 0.3, 0.4
        self.path = [(self.x, self.y)]
        self.collision_points = []
        self.running = True

    def set_slope(self, m):
        if m == 0:
            self.vx, self.vy = 1.0, 0.0
        else:
            self.vx = 1.0
            self.vy = m
            norm = np.sqrt(self.vx**2 + self.vy**2)
            self.vx /= norm
            self.vy /= norm

    def step(self):
        if not self.running:
            return

        tx, ty = np.inf, np.inf

        if self.vx > 0:
            tx = (1 - self.x) / self.vx
        elif self.vx < 0:
            tx = (0 - self.x) / self.vx

        if self.vy > 0:
            ty = (1 - self.y) / self.vy
        elif self.vy < 0:
            ty = (0 - self.y) / self.vy

        t = min(tx, ty)

        self.x += self.vx * t
        self.y += self.vy * t

        collided = False

        if abs(self.x - 0) < 1e-9 or abs(self.x - 1) < 1e-9:
            self.vx *= -1
            collided = True

        if abs(self.y - 0) < 1e-9 or abs(self.y - 1) < 1e-9:
            self.vy *= -1
            collided = True

        self.path.append((self.x, self.y))

        if collided:
            self.collision_points.append((self.x, self.y))


# =========================
# INIT
# =========================
sim = Billiard()
mode = "continuous"
show_heatmap = False

# =========================
# TKINTER UI
# =========================
root = tk.Tk()
root.title("Billiards Visual Lab 🎨")

entry = tk.Entry(root)
entry.insert(0, "sqrt(2)")
entry.pack()

def apply():
    val = parse_input(entry.get())
    if val is not None:
        sim.set_slope(val)
        sim.reset()

tk.Button(root, text="Apply Slope", command=apply).pack()

def toggle_mode():
    global mode
    mode = "collision" if mode == "continuous" else "continuous"

tk.Button(root, text="Toggle Mode", command=toggle_mode).pack()

def toggle_heat():
    global show_heatmap
    show_heatmap = not show_heatmap

tk.Button(root, text="Toggle Heatmap", command=toggle_heat).pack()

tk.Button(root, text="Reset", command=sim.reset).pack()

# =========================
# COLOR CONTROLS 🎛
# =========================
def set_bg():
    theme["bg"] = bg_entry.get()
    fig.patch.set_facecolor(theme["bg"])
    ax.set_facecolor(theme["bg"])

def set_traj():
    theme["trajectory"] = traj_entry.get()

def set_points():
    theme["points"] = point_entry.get()

tk.Label(root, text="Background").pack()
bg_entry = tk.Entry(root)
bg_entry.insert(0, "#0e1117")
bg_entry.pack()
tk.Button(root, text="Apply BG", command=set_bg).pack()

tk.Label(root, text="Trajectory Color").pack()
traj_entry = tk.Entry(root)
traj_entry.insert(0, "cyan")
traj_entry.pack()
tk.Button(root, text="Apply Trajectory", command=set_traj).pack()

tk.Label(root, text="Point Color").pack()
point_entry = tk.Entry(root)
point_entry.insert(0, "red")
point_entry.pack()
tk.Button(root, text="Apply Points", command=set_points).pack()

# =========================
# PLOT
# =========================
fig, ax = plt.subplots()
fig.patch.set_facecolor(theme["bg"])
ax.set_facecolor(theme["bg"])

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_aspect('equal')

line, = ax.plot([], [], lw=1, color=theme["trajectory"])
points = ax.scatter([], [], c=theme["points"], s=10)

heat = np.zeros((100,100))
img = ax.imshow(heat, extent=[0,1,0,1],
                origin='lower', alpha=0.6,
                cmap=theme["heatmap"])

# =========================
# UPDATE
# =========================
def update(frame):
    for _ in range(3):
        sim.step()

    if mode == "continuous":
        xs = [p[0] for p in sim.path]
        ys = [p[1] for p in sim.path]

        line.set_data(xs, ys)
        line.set_color(theme["trajectory"])

        points.set_offsets(np.empty((0,2)))

    else:
        if sim.collision_points:
            pts = np.array(sim.collision_points)
            points.set_offsets(pts)
            points.set_color(theme["points"])

        line.set_data([], [])

    if show_heatmap:
        x, y = sim.x, sim.y
        heat[int(y*99), int(x*99)] += 1
        img.set_data(heat)
        img.set_visible(True)
    else:
        img.set_visible(False)

    return line, points, img

ani = FuncAnimation(fig, update, interval=30)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()