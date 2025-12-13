import tkinter as tk
from tkinter import Toplevel, messagebox
from collections import deque
def check_bipartite_gui(app):
    """
    Kiểm tra đồ thị 2 phía (Bipartite) và highlight node trên canvas.
    app: instance của GraphApp
    """
    if not app.nodes:
        messagebox.showwarning("Cảnh báo", "Chưa có đỉnh nào!")
        return

    adj = {n[0]: [] for n in app.nodes}
    for u, v, w in app.edges:
        adj[u].append((v, w))
        if not app.is_directed:
            adj[v].append((u, w))

    color = {}
    is_bipartite = True

    for s in adj:
        if s not in color:
            color[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                # Highlight node đang duyệt
                highlight_node(app, u, color="orange")
                app.root.update()
                app.root.after(250)

                for v, _ in adj[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break

    if is_bipartite:
        messagebox.showinfo("Kết quả", "Đồ thị là 2 phía (Bipartite)!")
    else:
        messagebox.showinfo("Kết quả", "Không phải đồ thị 2 phía!")

def highlight_node(app, node_id, color="orange"):
    """Tô màu node trên canvas theo ID."""
    if node_id < 1 or node_id > len(app.nodes):
        return
    x = app.nodes[node_id - 1][1]
    y = app.nodes[node_id - 1][2]
    r = 18
    app.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)
    app.canvas.create_text(x, y, text=str(node_id), font=("Arial", 12, "bold"))
    app.canvas.update()
