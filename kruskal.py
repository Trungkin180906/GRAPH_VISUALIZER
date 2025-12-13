import tkinter as tk
from tkinter import Toplevel, messagebox


class KruskalSolver:
    def __init__(self, app):
        """
        app: GraphApp (canvas, nodes, edges, root)
        """
        self.app = app

    # ================= GUI =================
    def reset_highlight(self):
        self.app.canvas.delete("highlight")

    def highlight_edge(self, u, v, color="#FFD700", width=4):
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

        self.app.canvas.tag_raise(f"node_{u}")
        self.app.canvas.tag_raise(f"node_{v}")

    # ================= KRUSKAL =================
    def run(self):
        # Lấy danh sách đỉnh
        nodes = [n[0] for n in self.app.nodes]

        # Union-Find
        parent = {n: n for n in nodes}

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
            return True

        # Sắp xếp cạnh theo trọng số
        edges = sorted(self.app.edges, key=lambda x: x[2])

        mst_weight = 0
        edge_count = 0

        for u, v, w in edges:
            if union(u, v):
                mst_weight += w
                edge_count += 1

                self.highlight_edge(u, v)
                self.app.root.update()
                self.app.root.after(400)

                if edge_count == len(nodes) - 1:
                    break

        messagebox.showinfo(
            "Kruskal",
            f"Cây khung nhỏ nhất hoàn tất\nTổng trọng số: {mst_weight}"
        )

def run_kruskal_gui(app):
    win = Toplevel(app.root)
    win.title("Kruskal")

    tk.Label(
        win,
        text="Thuật toán Kruskal\n(Không cần chọn đỉnh bắt đầu)",
        justify="center"
    ).pack(pady=10)

    def start():
        solver = KruskalSolver(app)
        solver.reset_highlight()
        solver.run()

    tk.Button(
        win,
        text="Chạy Kruskal",
        command=start,
        bg="#FFD700"
    ).pack(pady=10)
