# canvas_area.py
import tkinter as tk

class CanvasArea(tk.Frame):#tạo 1 lớp kế thừa từ 1 khung chung cho cả nhóm
    def __init__(self, parent):
        super().__init__(parent, bg="white")#tạo khung với backgroud màu trắng
        #tạo canvas
        self.canvas=tk.Canvas(
            self, bg="white",#nền trắng
            highlightthickness=1,
            highlightbackground="#cccccc"#viền có màu xám nhạt
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)#canvas mở rộng đầy khung theo chiều ngang và dọc
        #văn bảng mặc định
        self.canvas.create_text(300,200,#vẽ văn bản trên canvas
            text="Khu vực hiển thị tòa nhà / đồ thị\n(Chưa thêm chức năng)",
            font=("Arial", 16),
            fill="gray"#chữ màu xám
        )
    def get_canvas(self):#trả về object canvas bên trong khung
        return self.canvas
        
    def dang_ky_node(self, ten_node, id_ve):
        """
        Luu lai ID ve node tren canvas de to sang khi duyet BFS/DFS.
        ten_node : ten dinh (A, B, C,...)
        id_ve    : gia tri tra ve cua canvas.create_oval(...)
        """
        if not hasattr(self, "danh_sach_node"):
            self.danh_sach_node = {}  # tao khi lan dau dung
        self.danh_sach_node[ten_node] = id_ve

    def to_sang(self, ten_node, mau="yellow"):
        """
        To sang mot node tren do thi trong thoi gian ngan.
        """
        if not hasattr(self, "danh_sach_node") or ten_node not in self.danh_sach_node:
            print(f"Khong tim thay node {ten_node} de to sang")
            return

        id_ve = self.danh_sach_node[ten_node]

        # đổi màu node
        self.canvas.itemconfig(id_ve, fill=mau)
        self.canvas.update()

        # tự chuyển lại sau 400ms
        self.canvas.after(400, lambda: self.canvas.itemconfig(id_ve, fill="white"))

