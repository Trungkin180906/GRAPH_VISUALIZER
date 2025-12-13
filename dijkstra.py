import tkinter as tk
from tkinter import messagebox, Toplevel
import heapq
class DijkstraSolver:
    def __init__(self, nodes, edges, is_directed):
        self.nodes = nodes
        self.edges = edges
        self.is_directed = is_directed

    def shortest_path(self, start, end):
        adj = {n[0]: [] for n in self.nodes}
        for u, v, w in self.edges:
            adj[u].append((v, w))
            if not self.is_directed:
                adj[v].append((u, w))

        dist = {n[0]: float("inf") for n in self.nodes}
        prev = {}#THÊM
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u#THÊM
                    heapq.heappush(pq, (dist[v], v))

        if start == end:
            return 0, [start]

        if end not in prev:
            return None, None

        # truy ngược đường đi
        path = []
        cur = end
        while cur != start:
            path.append(cur)
            cur = prev[cur]
        path.append(start)
        path.reverse()

        return dist[end], path

def highlight_edge(app, u, v, color="orange", width=4):
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


def run_dijkstra_gui(app):
    win = Toplevel(app.root)
    win.title("Dijkstra")

    tk.Label(win, text="ID bắt đầu").pack()
    e1 = tk.Entry(win)
    e1.pack()

    tk.Label(win, text="ID kết thúc").pack()
    e2 = tk.Entry(win)
    e2.pack()

    def run():
        try:
            s = int(e1.get())
            t = int(e2.get())
        except:
            messagebox.showerror("Lỗi", "Nhập số!")
            return

        app.canvas.delete("highlight")

        solver = DijkstraSolver(
            app.nodes,
            app.edges,
            app.is_directed
        )

        dist, path = solver.shortest_path(s, t)

        if path is None:
            messagebox.showinfo("Kết quả", "Không có đường đi")
            return

        # highlight từng cạnh
        for i in range(len(path) - 1):
            highlight_edge(app, path[i], path[i + 1])
            app.root.update()
            app.root.after(300)

        messagebox.showinfo(
            "Kết quả",
            f"Độ dài ngắn nhất: {dist}\n"
            f"Đường đi: {' → '.join(map(str, path))}"
        )

    tk.Button(win, text="Chạy", command=run).pack(pady=10)
