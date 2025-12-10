import tkinter as tk
from tkinter import filedialog, messagebox
import json

class GraphApp:#lớp quản lý giao diện đồ thị
    def __init__(self, root):
        self.root = root#tạo cửa sổ hiển thị
        self.root.title("Hệ thống phân tích đường đi trong trường học")#tiêu đề

        self.nodes = []#thuộc tính node(phòng: id, x, y)
        self.edges = []#thuộc tính cạnh(hành lang: u, v, w), w=trọng số, u,v=id node
        self.is_directed = False#mặc định là vô hướng

        #khung phải canvas
        self.canvas = tk.Canvas(root, width=700, height=600, bg="white")#tạo khung để vẽ đồ thị mặc định khung màu trắng
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)#bố cục nằm bên phải

        # Button-1 nhấp chuột trái để vẽ node
        self.canvas.bind("<Button-1>", self.add_node)

        #khung trái menu
        left_frame = tk.Frame(root)
        left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        title = tk.Label(left_frame, text="CHỨC NĂNG", font=("Arial", 14, "bold"))
        title.pack(pady=10)#tạo bố cục cho dòng chữ tiêu đề không bị dính sát viền dưới

        # Chọn đồ thị có hướng / vô hướng
        tk.Label(left_frame, text="Chế độ đồ thị:").pack()#tạo tiêu đề cho đồ thị
        self.graph_type = tk.StringVar(value="undirected")#mặc định là vô hướng
        tk.Radiobutton(left_frame, text="Vô hướng", variable=self.graph_type, value="undirected",
                       command=self.update_direction).pack(anchor="w")
        tk.Radiobutton(left_frame, text="Có hướng", variable=self.graph_type, value="directed",
                       command=self.update_direction).pack(anchor="w")

        tk.Label(left_frame, text="").pack()  # khoảng cách

        btn_add_edge = tk.Button(left_frame, text="Thêm cạnh", width=20, command=self.add_edge_window)
        btn_add_edge.pack(pady=5)

        btn_save = tk.Button(left_frame, text="Lưu đồ thị", width=20, command=self.save_graph)
        btn_save.pack(pady=5)

        btn_load = tk.Button(left_frame, text="Tải đồ thị", width=20, command=self.load_graph)
        btn_load.pack(pady=5)

    def update_direction(self):#cập nhật đồ thị có hướng
        self.is_directed = (self.graph_type.get() == "directed")#phải cập nhật lại bởi vì đồ thị đang mặc định là vô hướng

    def add_node(self, event):#vẽ node(phòng)
        x, y = event.x, event.y#lấy tọa độ chuột click (tọa độ ngang =x, tọa độ dọc=y)
        node_id = len(self.nodes) + 1#độ dài của node có bnhieu đỉnh 
        self.nodes.append((node_id, x, y))
        r = 18#kích thước bán kính của đỉnh
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="skyblue")#góc trái (x-r,y-r) goc phải(x+r,y+r)
        self.canvas.create_text(x, y, text=str(node_id), font=("Arial", 12, "bold"))#giúp người dùng phân biệt được đâu là đỉnh 1 đâu là đỉnh 2

    def add_edge_window(self):#thêm cạnh(hành lang)
        if len(self.nodes)<2:#bắt buộc 2 nối cạnh giữa 2 đỉnh 
            messagebox.showwarning("Cảnh báo", "Cần ít nhất 2 phòng để tạo cạnh!")
            return

        win = tk.Toplevel(self.root)
        win.title("Thêm cạnh")

        tk.Label(win, text="Node 1:").pack()#tạo các nhãn
        entry_u = tk.Entry(win)#tạo các ô nhập liệu
        entry_u.pack()

        tk.Label(win, text="Node 2:").pack()
        entry_v = tk.Entry(win)
        entry_v.pack()

        tk.Label(win, text="Trọng số (khoảng cách):").pack()
        entry_w = tk.Entry(win)
        entry_w.pack()

        def add_edge():#hàm con của add...window nó chỉ chạy user bấm nút thêm
            try:
                u = int(entry_u.get())#entry.get lấy vb user nhập vào dạng chuỗi
                v = int(entry_v.get())
                w = float(entry_w.get())
            except:#nếu user nhập abc thay vì số thì câu lệnh sẽ in ra thông báo thay vì văng ra lỗi
                messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ!")
                return

            if u<1 or v<1 or u>len(self.nodes) or v>len(self.nodes):
                messagebox.showerror("Lỗi", "Node không tồn tại!")
                return

            self.edges.append((u, v, w))#lưu vào ds cạnh

            # Vẽ cạnh
            x1, y1 = self.nodes[u - 1][1], self.nodes[u - 1][2]
            x2, y2 = self.nodes[v - 1][1], self.nodes[v - 1][2]

            #hiển trị trực quan đồ thị
            self.canvas.create_line(x1, y1, x2, y2, width=2)#(x1,y1=node1),(x2,y2=node2)
            self.canvas.create_text((x1+x2)//2, (y1+y2)//2, text=str(w), fill="red")#tính vị trí trung điểm 

            # Nếu là đồ thị có hướng, vẽ mũi tên
            if self.is_directed:
                self.draw_arrow(x1, y1, x2, y2)

            win.destroy()

        tk.Button(win, text="Thêm", command=add_edge).pack(pady=10)

    def draw_arrow(self, x1, y1, x2, y2):#vẽ mũi tên
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)

    def save_graph(self):#lưu đồ thị
        data = {
            "directed": self.is_directed,
            "nodes": [{"id": n[0], "x": n[1], "y": n[2]} for n in self.nodes],
            "edges": [{"u": u, "v": v, "w": w} for (u, v, w) in self.edges]
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON Files", "*.json")])
        if not file_path:
            return

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Thành công", "Đã lưu đồ thị thành công!")

    def load_graph(self):#tải đồ thị
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if not file_path:
            return

        with open(file_path, "r") as f:
            data = json.load(f)

        # Reset
        self.canvas.delete("all")
        self.nodes.clear()
        self.edges.clear()

        self.is_directed = data.get("directed", False)
        self.graph_type.set("directed" if self.is_directed else "undirected")

        # Load nodes
        for node in data["nodes"]:
            nid, x, y = node["id"], node["x"], node["y"]
            self.nodes.append((nid, x, y))
            r = 18
            self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="skyblue")
            self.canvas.create_text(x, y, text=str(nid), font=("Arial", 12, "bold"))

        # Load edges
        for e in data["edges"]:
            u, v, w = e["u"], e["v"], e["w"]
            self.edges.append((u, v, w))

            x1, y1 = self.nodes[u - 1][1], self.nodes[u - 1][2]
            x2, y2 = self.nodes[v - 1][1], self.nodes[v - 1][2]

            self.canvas.create_line(x1, y1, x2, y2, width=2)
            self.canvas.create_text((x1+x2)//2, (y1+y2)//2, text=str(w), fill="red")

            if self.is_directed:
                self.draw_arrow(x1, y1, x2, y2)

