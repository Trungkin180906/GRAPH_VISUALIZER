import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button
from collections import deque

class MaxFlowSolver:
    def __init__(self, n, graph_matrix):
        """
        n: Số lượng đỉnh
        graph_matrix: Ma trận trọng số (Dung lượng)
        """
        self.ROW = n
        self.graph = [row[:] for row in graph_matrix] # Copy để không sửa matrix gốc

    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = deque()
        queue.append(s)
        visited[s] = True
        parent[s] = -1

        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def get_max_flow(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        all_paths = []  #lưu các đường tăng luồng

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            v = sink
            path = []

            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                path.append((u, v))
                v = u

            path.reverse()
            all_paths.append(path)

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            max_flow += path_flow
        return max_flow, all_paths

def highlight_edge(app, u, v, color="red", width=4):
    n1 = next(n for n in app.nodes if n[0] == u)
    n2 = next(n for n in app.nodes if n[0] == v)

    x1, y1 = n1[1], n1[2]
    x2, y2 = n2[1], n2[2]

    app.canvas.create_line(
        x1, y1, x2, y2,
        fill=color,
        width=width,
        tags="highlight"
    )

    app.canvas.tag_raise(f"node_{u}")
    app.canvas.tag_raise(f"node_{v}")

# --- Hàm cầu nối GUI ---
def run_ford_fulkerson_gui(app):
    nodes = app.nodes
    edges = app.edges
    is_directed = app.is_directed

    dialog = Toplevel(app.root)
    dialog.title("Tính Luồng Cực Đại (Max Flow)")
    dialog.geometry("300x200")

    tk.Label(dialog, text="Nhập ID điểm bắt đầu (Source):").pack(pady=5)
    entry_s = tk.Entry(dialog)
    entry_s.pack(pady=5)

    tk.Label(dialog, text="Nhập ID điểm kết thúc (Sink):").pack(pady=5)
    entry_t = tk.Entry(dialog)
    entry_t.pack(pady=5)

    def on_calculate():
        try:
            s_id = int(entry_s.get())
            t_id = int(entry_t.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Nhập số nguyên!")
            return

        node_ids = [n[0] for n in nodes]
        if s_id not in node_ids or t_id not in node_ids:
            messagebox.showerror("Lỗi", "ID không tồn tại!")
            return

        id_to_index = {n[0]: i for i, n in enumerate(nodes)}
        n = len(nodes)
        matrix = [[0]*n for _ in range(n)]

        for u, v, w in edges:
            ui, vi = id_to_index[u], id_to_index[v]
            matrix[ui][vi] = w
            if not is_directed:
                matrix[vi][ui] = w

        solver = MaxFlowSolver(n, matrix)
        max_flow, paths = solver.get_max_flow(
            id_to_index[s_id],
            id_to_index[t_id]
        )

        # xoá highlight cũ
        app.canvas.delete("highlight")

        # highlight từng đường tăng luồng
        for path in paths:
            for u_idx, v_idx in path:
                u_id = nodes[u_idx][0]
                v_id = nodes[v_idx][0]
                highlight_edge(app, u_id, v_id)
                app.root.update()
                app.root.after(300)

        messagebox.showinfo(
            "Kết quả",
            f"Luồng cực đại từ {s_id} → {t_id} = {max_flow}"
        )
        dialog.destroy()
    tk.Button(dialog, text="Tính toán", command=on_calculate, bg="skyblue").pack(pady=15)
