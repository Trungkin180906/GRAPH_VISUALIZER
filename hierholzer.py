import copy
import tkinter as tk
from tkinter import Toplevel, messagebox

class HierholzerSolver:
    def __init__(self, app, graph):
        self.app = app
        self.graph = copy.deepcopy(graph)

    # Xóa highlight cũ
    def reset_highlight(self):
        self.app.canvas.delete("highlight")

    # Highlight cạnh
    def highlight_edge(self, u, v, color="blue", width=4):
        n1 = next(n for n in self.app.nodes if n[0] == u)
        n2 = next(n for n in self.app.nodes if n[0] == v)
        x1, y1 = n1[1], n1[2]
        x2, y2 = n2[1], n2[2]
        self.app.canvas.create_line(x1, y1, x2, y2, fill=color, width=width, tags="highlight")
        self.app.canvas.tag_raise(f"node_{u}")
        self.app.canvas.tag_raise(f"node_{v}")
        self.app.root.update()
        self.app.root.after(300)

    # Thuật toán Hierholzer
    def run_algorithm(self, start):
        stack = [start]
        circuit = []
        while stack:
            u = stack[-1]
            if self.graph[u]:
                v = self.graph[u].pop()
                self.graph[v].remove(u)
                self.highlight_edge(u, v)
                stack.append(v)
            else:
                circuit.append(stack.pop())
        return circuit[::-1]

# ================= GUI =================
def run_hierholzer_gui(app):
    win = Toplevel(app.root)
    win.title("Hierholzer - Euler Path/Circuit")

    tk.Label(win, text="Chọn loại đường đi Euler", justify="center").pack(pady=10)

    # Chuyển nodes/edges sang adjacency list
    graph = {n[0]: [] for n in app.nodes}
    for u, v, w in app.edges:
        graph[u].append(v)
        graph[v].append(u)  # vô hướng

    solver = HierholzerSolver(app, graph)
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

    tk.Button(win, text="Chạy", command=run, bg="blue", fg="white").pack(pady=10)
