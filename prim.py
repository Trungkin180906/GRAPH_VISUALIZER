import tkinter as tk
from tkinter import Toplevel, messagebox
import heapq

class PrimSolver:
    def __init__(self, app):
        """
        app: GraphApp (có canvas, nodes, edges, root)
        """
        self.app = app

    def reset_highlight(self):
        self.app.canvas.delete("highlight")

    def highlight_edge(self, u, v, color="green", width=4):
        n1 = next(n for n in self.app.nodes if n[0] == u)
        n2 = next(n for n in self.app.nodes if n[0] == v)

        x1, y1 = n1[1], n1[2]
        x2, y2 = n2[1], n2[2]

        self.app.canvas.create_line(
            x1, y1, x2, y2,
            fill=color,
            width=width,
            tags="highlight"
        )

        # Đưa node lên trên
        self.app.canvas.tag_raise(f"node_{u}")
        self.app.canvas.tag_raise(f"node_{v}")

    def run(self, start):
        adj = {n[0]: [] for n in self.app.nodes}
        for u, v, w in self.app.edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Prim CHỈ dùng cho đồ thị vô hướng

        visited = set([start])
        pq = []

        for v, w in adj[start]:
            heapq.heappush(pq, (w, start, v))

        mst_weight = 0

        while pq:
            w, u, v = heapq.heappop(pq)

            if v in visited:
                continue

            visited.add(v)
            mst_weight += w

            self.highlight_edge(u, v)
            self.app.root.update()
            self.app.root.after(400)

            for next_v, next_w in adj[v]:
                if next_v not in visited:
                    heapq.heappush(pq, (next_w, v, next_v))

        messagebox.showinfo(
            "Prim",
            f"Cây khung nhỏ nhất hoàn tất\nTổng trọng số: {mst_weight}"
        )

def run_prim_gui(app):
    win = Toplevel(app.root)
    win.title("Prim")

    tk.Label(win, text="ID đỉnh bắt đầu").pack(pady=5)
    entry = tk.Entry(win)
    entry.pack(pady=5)

    def start_prim():
        try:
            s = int(entry.get())
        except:
            messagebox.showerror("Lỗi", "Nhập số nguyên!")
            return

        node_ids = [n[0] for n in app.nodes]
        if s not in node_ids:
            messagebox.showerror("Lỗi", "ID không tồn tại!")
            return

        solver = PrimSolver(app)
        solver.reset_highlight()
        solver.run(s)

    tk.Button(win, text="Chạy", command=start_prim).pack(pady=10)
