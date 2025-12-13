import tkinter as tk
from tkinter import messagebox, Toplevel
from collections import deque
# HIGHLIGHT NODE TRÊN CANVAS
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

# BUILD ADJ
def build_adj(nodes, edges, directed):
    adj = {n[0]: [] for n in nodes}
    for u, v, w in edges:
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj

# BFS LOGIC
def bfs_logic(start, nodes, edges, directed, app):
    adj = build_adj(nodes, edges, directed)
    visited = set()
    q = deque([start])
    order = []

    while q:
        u = q.popleft()
        if u not in visited:
            visited.add(u)
            order.append(u)

            highlight_node(app, u, "orange")
            app.root.after(250)

            for v, _ in adj[u]:
                if v not in visited:
                    q.append(v)

    return order

# DFS LOGIC
def dfs_logic(start, nodes, edges, directed, app):
    adj = build_adj(nodes, edges, directed)
    visited = set()
    order = []

    def explore(u):
        visited.add(u)
        order.append(u)
        highlight_node(app, u, "orange")
        app.root.after(250)

        for v, _ in adj[u]:
            if v not in visited:
                explore(v)

    explore(start)
    return order

# GUI BFS WINDOW
def run_bfs_gui(app):
    if len(app.nodes) < 1:
        messagebox.showwarning("Cảnh báo", "Chưa có đỉnh nào!")
        return

    dialog = Toplevel(app.root)
    dialog.title("Duyệt BFS")
    dialog.geometry("300x150")

    tk.Label(dialog, text="Nhập ID đỉnh bắt đầu:").pack(pady=5)
    entry_s = tk.Entry(dialog)
    entry_s.pack(pady=5)

    def on_run():
        try:
            s = int(entry_s.get())
        except:
            messagebox.showerror("Lỗi", "Nhập số hợp lệ!")
            return

        if s < 1 or s > len(app.nodes):
            messagebox.showerror("Lỗi", "ID đỉnh không tồn tại!")
            return

        result = bfs_logic(s, app.nodes, app.edges, app.is_directed, app)
        messagebox.showinfo("Kết quả BFS", " → ".join(map(str, result)))
        dialog.destroy()

    tk.Button(dialog, text="Chạy BFS", command=on_run, bg="skyblue").pack(pady=10)

# GUI DFS WINDOW
def run_dfs_gui(app):
    if len(app.nodes) < 1:
        messagebox.showwarning("Cảnh báo", "Chưa có đỉnh nào!")
        return

    dialog = Toplevel(app.root)
    dialog.title("Duyệt DFS")
    dialog.geometry("300x150")

    tk.Label(dialog, text="Nhập ID đỉnh bắt đầu:").pack(pady=5)
    entry_s = tk.Entry(dialog)
    entry_s.pack(pady=5)

    def on_run():
        try:
            s = int(entry_s.get())
        except:
            messagebox.showerror("Lỗi", "Nhập số hợp lệ!")
            return

        if s < 1 or s > len(app.nodes):
            messagebox.showerror("Lỗi", "ID đỉnh không tồn tại!")
            return

        result = dfs_logic(s, app.nodes, app.edges, app.is_directed, app)
        messagebox.showinfo("Kết quả DFS", " → ".join(map(str, result)))
        dialog.destroy()
    tk.Button(dialog, text="Chạy DFS", command=on_run, bg="skyblue").pack(pady=10)
