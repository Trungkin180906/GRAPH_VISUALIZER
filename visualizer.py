import tkinter as tk
class Graphvisualizer:
    def __init__(self, title="Graph visualazer"):
        self.root=tk.Tk()#tạo cửa sổ
        self.root.title(title)#tên tiêu đề
        self.canvas=tk.Canvas(self.root, width=800, height=600, bg="White")#tạo khung và trang màu để bảng đồ thị
        self.canvas.pack()#hiển thị canvas lên màn hình (pack quản lý bố cục)

    def draw_node(self, x, y, text, color="white"):#hàm vẽ đỉnh tại vị trí x, y 
        r=20#đỉnh có bán kính là 20
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, width=2)#
        self.canvas.create_text(x, y, text=str(text))

    def draw_edge(self, x1, y1, x2, y2, weight, color="black"):#hàm vẽ cạnh
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
        min_x=(x1+x2)/2
        min_y=(y1+y2)/2
        self.canvas.create_text(min_x, min_y, text=str(weight), fill="blue")

    def show(self):#hàm chạy 
        self.root.mainloop()
