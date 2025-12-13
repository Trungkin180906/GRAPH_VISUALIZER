# main.py
import tkinter as tk
from interface_screen import LeftInterface
from canvas import CanvasArea
from load_save import GraphApp

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Phân tích đường đi trong tòa nhà – Trường Đại Học XYZ")
        self.geometry("1200x700")

        # Frame chính
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # CANVAS
        canvas = CanvasArea(main_frame)
        canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # TRUYỀN CANVAS VÀO MENU
        left = LeftInterface(main_frame, canvas)
        left.pack(side=tk.LEFT, fill=tk.Y)

if __name__ == "__main__":
    app=MainWindow()
    app.mainloop()
