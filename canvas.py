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
