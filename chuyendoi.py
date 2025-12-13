import tkinter as tk
from tkinter import ttk, messagebox

# CÁC HÀM CHUYỂN ĐỔI
def edges_to_adj_list(n, edges, is_directed):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        if not is_directed:
            adj[v].append((u, w))
    return adj

def edges_to_adj_matrix(n, edges, is_directed):
    mat = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v, w in edges:
        mat[u][v] = w
        if not is_directed:
            mat[v][u] = w
    return mat

def adj_list_to_edges(adj, is_directed):
    edges = []
    for u in range(1, len(adj)):
        for v, w in adj[u]:
            if is_directed or u < v:
                edges.append((u, v, w))
    return edges

def adj_list_to_adj_matrix(adj, is_directed):
    n = len(adj) - 1
    mat = [[0] * (n + 1) for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v, w in adj[u]:
            mat[u][v] = w
            if not is_directed:
                mat[v][u] = w
    return mat

def matrix_to_adj_list(mat):
    n = len(mat)
    adj = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                adj[i + 1].append((j + 1, mat[i][j]))
    return adj

def matrix_to_edges(mat, is_directed):
    n = len(mat)
    edges = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                if is_directed or i < j:
                    edges.append((i + 1, j + 1, mat[i][j]))
    return edges

# HÀM HIỂN THỊ
def matrix_to_string(mat):
    n = len(mat)
    header = "    " + " ".join(f"{j+1:>4}" for j in range(n))
    rows = "\n".join(
        f"{i+1:>2} |" + " ".join(f"{mat[i][j]:>4}" for j in range(n))
        for i in range(n)
    )
    return header + "\n" + rows

def adj_to_string(adj):
    return "\n".join(
        f"{i}: " + ", ".join(f"{v}(w={w})" for v, w in adj[i])
        for i in range(1, len(adj))
    )

def edges_to_string(edges):
    return "\n".join(f"{u} {v} {w}" for u, v, w in edges)

# CỬA SỔ BIỂU DIỄN & CHUYỂN ĐỔI
def show_representations(nodes, edges, is_directed):
    if not nodes:
        messagebox.showwarning("Lỗi", "Chưa có đồ thị!")
        return

    n = len(nodes)
    win = tk.Toplevel()
    win.title("Biểu diễn & Chuyển đổi đồ thị")
    win.geometry("780x640")

    notebook = ttk.Notebook(win)
    notebook.pack(fill="both", expand=True)

    # TAB 1: BIỂU DIỄN TỪ ĐỒ THỊ VẼ (KHÔNG POPUP)
    tab_view = ttk.Frame(notebook)
    notebook.add(tab_view, text="Biểu diễn đồ thị")

    tk.Label(tab_view, text="BIỂU DIỄN TỪ ĐỒ THỊ VẼ",
             font=("Arial", 11, "bold")).pack(pady=5)

    view_output = tk.Text(tab_view, height=18, bg="#f2f2f2")
    view_output.pack(fill="both", padx=10, pady=5)

    def show_view(text):
        view_output.delete("1.0", "end")
        view_output.insert("1.0", text)

    def show_edges_view():
        show_view("DANH SÁCH CẠNH\n" + edges_to_string(edges))

    def show_adj_view():
        adj = edges_to_adj_list(n, edges, is_directed)
        show_view("DANH SÁCH KỀ\n" + adj_to_string(adj))

    def show_matrix_view():
        mat = edges_to_adj_matrix(n, edges, is_directed)
        mat0 = [row[1:] for row in mat[1:]]
        show_view("MA TRẬN KỀ\n" + matrix_to_string(mat0))

    ttk.Button(tab_view, text="Danh sách cạnh", width=30,
               command=show_edges_view).pack(pady=3)
    ttk.Button(tab_view, text="Danh sách kề", width=30,
               command=show_adj_view).pack(pady=3)
    ttk.Button(tab_view, text="Ma trận kề", width=30,
               command=show_matrix_view).pack(pady=3)

    # TAB 2: CHUYỂN ĐỔI BIỂU DIỄN (3 Ô NHẬP RIÊNG)
    tab_convert = ttk.Frame(notebook)
    notebook.add(tab_convert, text="Chuyển đổi biểu diễn")

    frame_input = ttk.Frame(tab_convert)
    frame_input.pack(fill="x", pady=10)

    # ----- DS CẠNH ----
    ttk.Label(frame_input, text="Danh sách cạnh (u v w)").grid(row=0, column=0)
    edge_box = tk.Text(frame_input, height=7, width=25)
    edge_box.grid(row=1, column=0, padx=5)
    edge_box.insert("1.0", "1 2 3\n2 3 5\n3 1 2")

    # ----- DS KỀ -----
    ttk.Label(frame_input, text="Danh sách kề").grid(row=0, column=1)
    adj_box = tk.Text(frame_input, height=7, width=25)
    adj_box.grid(row=1, column=1, padx=5)
    adj_box.insert("1.0", "1: 2 3\n2: 1\n3: 1")

    # ----- MA TRẬN -----
    ttk.Label(frame_input, text="Ma trận kề").grid(row=0, column=2)
    mat_box = tk.Text(frame_input, height=7, width=25)
    mat_box.grid(row=1, column=2, padx=5)
    mat_box.insert("1.0", "0 1 1\n1 0 0\n1 0 0")

    # ----- OUTPUT -----
    ttk.Label(tab_convert, text="KẾT QUẢ",
              font=("Arial", 11, "bold")).pack(pady=5)

    output_box = tk.Text(tab_convert, height=12, bg="#f2f2f2")
    output_box.pack(fill="both", padx=10)

    def show_output(text):
        output_box.delete("1.0", "end")
        output_box.insert("1.0", text)

    # ----- PARSE -----
    def get_edges():
        res = []
        for line in edge_box.get("1.0", "end").splitlines():
            if line.strip():
                res.append(tuple(map(int, line.split())))
        return res

    def get_adj():
        adj = [[] for _ in range(n + 1)]
        for line in adj_box.get("1.0", "end").splitlines():
            if ":" in line:
                u, vs = line.split(":")
                for v in vs.split():
                    adj[int(u)].append((int(v), 1))
        return adj

    def get_mat():
        mat = []
        for line in mat_box.get("1.0", "end").splitlines():
            if line.strip():
                mat.append(list(map(int, line.split())))
        return mat

    # ----- BUTTONS -----
    frame_btn = ttk.Frame(tab_convert)
    frame_btn.pack(pady=10)

    ttk.Button(frame_btn, text="DS cạnh → DS kề",
               command=lambda: show_output(
                   adj_to_string(edges_to_adj_list(n, get_edges(), is_directed)))
               ).grid(row=0, column=0, padx=5)

    ttk.Button(frame_btn, text="DS cạnh → Ma trận",
               command=lambda: show_output(
                   matrix_to_string(
                       [row[1:] for row in
                        edges_to_adj_matrix(n, get_edges(), is_directed)[1:]]))
               ).grid(row=0, column=1, padx=5)

    ttk.Button(frame_btn, text="DS kề → DS cạnh",
               command=lambda: show_output(
                   edges_to_string(adj_list_to_edges(get_adj(), is_directed)))
               ).grid(row=1, column=0, padx=5)

    ttk.Button(frame_btn, text="DS kề → Ma trận",
               command=lambda: show_output(
                   matrix_to_string(
                       [row[1:] for row in
                        adj_list_to_adj_matrix(get_adj(), is_directed)[1:]]))
               ).grid(row=1, column=1, padx=5)

    ttk.Button(frame_btn, text="Ma trận → DS kề",
               command=lambda: show_output(
                   adj_to_string(matrix_to_adj_list(get_mat())))
               ).grid(row=2, column=0, padx=5)

    ttk.Button(frame_btn, text="Ma trận → DS cạnh",
               command=lambda: show_output(
                   edges_to_string(matrix_to_edges(get_mat(), is_directed)))
               ).grid(row=2, column=1, padx=5)
