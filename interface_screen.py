import tkinter as tk#thư viện tạo giao diện
from tkinter import ttk#ttk cung cấp (button, lable,......)
class LeftInterface(tk.Frame):
    def __init__(self, parent, canvas_area):
        super().__init__(parent, width=250, bg="#e6e6e6")#tạo khung chiều rộng=250, nền xám nhạt
        self.pack_propagate(False)#giữ chiều rộng cố định
        self.canvas_area=canvas_area#tham chiếu đến canvas bên phải

        tk.Label(#tiêu đề chức năng
            self,
            text="Chức năng",
            font=("Arial", 14, "bold"),#from chữ in đậm
            bg="#e6e6e6"
        ).pack(pady=10)#thêm khoảng trống 10px trên dưới chức năng

        # Nút "Vẽ sơ đồ tòa nhà"
        btn_draw = ttk.Button(self, text="Vẽ /lưu sơ đồ tòa nhà", command=self.open_graph_window)#tạo nút nhấn trong khung giao diện
        btn_draw.pack(fill=tk.X, padx=15, pady=5)#định dạng nút nằm trên giao diện trái/phải=15, trên dưới=5

        # Các nút khác
        other_buttons = [
            "Tìm đường đi ngắn nhất",
            "Duyệt BFS / DFS",
            "Khám phá toàn bộ phòng",
            "Kiểm tra đồ thị 2 phía",
            "Chuyển đổi biểu diễn",
            "Tối ưu kết nối (Prim)",
            "Kết nối độc lập (Kruskal)",
            "Luồng người di chuyển (Ford-Fulkerson)",
            "Đi qua mỗi hành lang 1 lần (Fleury)",
            "Chu trình kín hoàn hảo (Hierholzer)"
        ]
        for name in other_buttons:
            ttk.Button(self, text=name).pack(fill=tk.X, padx=15, pady=5)#tương tự như nút trên 

    # Phương thức mở GraphApp (tạo hàm này khi nhấn vào nút được tạo ở trên nút đó sẽ gọi đến hàm này và thực hiện)
    def open_graph_window(self):
        from load_save import GraphApp
        win = tk.Toplevel(self)#tạo cửa sổ con mới
        win.title("Vẽ/lưu sơ đồ tòa nhà")#đặt tên cho cửa sổ con mới
        app = GraphApp(win)#khởi tạo interface trên interface main
