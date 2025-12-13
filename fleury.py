import copy
import tkinter as tk
from tkinter import Toplevel, messagebox

class FleurySolver:
    def __init__(self, app, graph):
        self.app = app
        self.graph = copy.deepcopy(graph)

    # Xóa highlight cũ
    def reset_highlight(self):
        self.app.canvas.delete("highlight")

    # Highlight cạnh
    def highlight_edge(self, u, v, color="red", width=4):
        n1 = next(n for n in self.app.nodes if n[0] == u)
        n2 = next(n for n in self.app.nodes if n[0] == v)
        x1, y1 = n1[1], n1[2]
        x2, y2 = n2[1], n2[2]
        self.app.canvas.create_line(x1, y1, x2, y2, fill=color, width=width, tags="highlight")
        self.app.canvas.tag_raise(f"node_{u}")
        self.app.canvas.tag_raise(f"node_{v}")
        self.app.root.update()
        self.app.root.after(400)

    # DFS để kiểm tra cạnh cầu
    def dfs(self, u, visited):
        visited.add(u)
        for v in self.graph[u]:
            if v not in visited:
                self.dfs(v, visited)

    def bridge_edges(self, u, v):
        visited = set()
        self.dfs(u, visited)
        dem1 = len(visited)

        # Xóa tạm cạnh
        self.graph[u].remove(v)
        self.graph[v].remove(u)

        visited = set()
        self.dfs(u, visited)
        dem2 = len(visited)

        # Khôi phục cạnh
        self.graph[u].append(v)
        self.graph[v].append(u)

        return dem2 < dem1

    # Thuật toán Fleury
    def run_algorithm(self, start):
        u = start
        path = [u]
        while self.graph[u]:
            for v in self.graph[u]:
                if len(self.graph[u]) == 1 or not self.bridge_edges(u, v):
                    self.highlight_edge(u, v)
                    self.graph[u].remove(v)
                    self.graph[v].remove(u)
                    u = v
                    path.append(u)
                    break
        return path

# ================= GUI =================
def run_fleury_gui(app):
    win = Toplevel(app.root)
    win.title("Fleury - Euler Path/Circuit")
    tk.Label(win, text="Chọn loại đường đi Euler", justify="center").pack(pady=10)

    # Chuyển nodes/edges sang adjacency list
    graph = {n[0]: [] for n in app.nodes}
    for u, v, w in app.edges:
        graph[u].append(v)
        graph[v].append(u)  # vô hướng

    solver = FleurySolver(app, graph)
    solver.reset_highlight()

    # Radio chọn loại đường đi
    choice_var = tk.StringVar()
    choice_var.set("circuit")  # mặc định chu trình

    tk.Radiobutton(win, text="Chu trình Euler", variable=choice_var, value="circuit").pack()
    tk.Radiobutton(win, text="Đường đi Euler", variable=choice_var, value="path").pack()

    def run():
        solver.reset_highlight()
        odd_nodes = [u for u in graph if len(graph[u]) % 2 == 1]

        if choice_var.get() == "circuit":
        # kiểm tra tất cả đỉnh bậc chẵn
            if any(len(graph[u]) % 2 != 0 for u in graph):
                messagebox.showerror("Lỗi", "Đồ thị không có chu trình Euler!")
                return
            start_node = list(graph.keys())[0]  # bất kỳ đỉnh nào cũng được
        else:  # đường đi Euler
            if len(odd_nodes) != 2:
                messagebox.showerror("Lỗi", "Đồ thị không có đường đi Euler!")
                return
            start_node = odd_nodes[0]

        path = solver.run_algorithm(start_node)
        messagebox.showinfo("Fleury", f"Đường đi Euler hoàn tất:\n{' → '.join(str(x) for x in path)}")

    tk.Button(win, text="Chạy", command=run, bg="red", fg="white").pack(pady=10)
