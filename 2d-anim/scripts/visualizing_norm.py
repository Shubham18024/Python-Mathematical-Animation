import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def setup_axes():
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_aspect("equal")
    ax.set_title("Unit Ball in Different Norms on ℝ²")
    return fig, ax

def lp_unit_ball(p, num_points=400):
    theta = np.linspace(0, 2*np.pi, num_points)

    if p == np.inf:
        n = num_points // 4
        x = np.concatenate([
            np.linspace(-1, 1, n),
            np.ones(n),
            np.linspace(1, -1, n),
            -np.ones(n)
        ])
        y = np.concatenate([
            np.ones(n),
            np.linspace(1, -1, n),
            -np.ones(n),
            np.linspace(-1, 1, n)
        ])
        return x[:num_points], y[:num_points]

    x = np.sign(np.cos(theta)) * (np.abs(np.cos(theta)) ** (2/p))
    y = np.sign(np.sin(theta)) * (np.abs(np.sin(theta)) ** (2/p))
    return x, y

def update(frame):
    ax.clear()

    p_index = frame // points_per_norm
    t_index = frame % points_per_norm
    current_p = p_values[p_index]

    x, y = lp_unit_ball(current_p)

    ax.plot(x, y, 'r', linewidth=2)
    ax.set_title(f"Unit Ball in ℓₚ for p = {current_p}")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)

    ax.plot(x[t_index], y[t_index], 'bo', markersize=8)

    return []

p_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.inf]
points_per_norm = 300
total_frames = len(p_values) * points_per_norm

fig, ax = setup_axes()

ani = animation.FuncAnimation(
    fig, update,
    frames=total_frames,
    interval=20,
    blit=False
)

plt.close(fig)

ani.save("lp_unit_balls.mp4", fps=30, dpi=100)
