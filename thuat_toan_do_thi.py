# ================================
# Thuật toán duyệt đồ thị: BFS & DFS
# ================================

from collections import deque
import time

class ThuatToanDoThi:
    def __init__(self, canvas):
        self.canvas = canvas
        self.toc_do = 0.6  # thời gian tô sáng mỗi đỉnh khi duyệt

    # ---------------------------------------
    # HÀM TÔ SÁNG 1 ĐỈNH (node)
    # ---------------------------------------
    def to_sang_dinh(self, dinh_id):
        # đổi màu đỉnh thành vàng
        self.canvas.itemconfig(dinh_id, fill="yellow")
        self.canvas.update()
        time.sleep(self.toc_do)

    # ---------------------------------------
    # HÀM BFS – Duyệt theo chiều rộng
    # ---------------------------------------
    def bfs(self, do_thi, dinh_bat_dau):
        """
        do_thi: dict dạng {dinh: [danh sách kề]}
        dinh_bat_dau: tên/ID đỉnh bắt đầu duyệt
        """

        hang_doi = deque()
        da_tham = set()

        hang_doi.append(dinh_bat_dau)
        da_tham.add(dinh_bat_dau)

        while hang_doi:
            dinh = hang_doi.popleft()

            # tô sáng đỉnh đang duyệt trên canvas
            if dinh in do_thi["canvas_id"]:
                self.to_sang_dinh(do_thi["canvas_id"][dinh])

            # duyệt hàng xóm
            for ke in do_thi["ke"][dinh]:
                if ke not in da_tham:
                    da_tham.add(ke)
                    hang_doi.append(ke)

        return da_tham

    # ---------------------------------------
    # HÀM DFS – Duyệt theo chiều sâu
    # ---------------------------------------
    def dfs(self, do_thi, dinh_bat_dau):
        da_tham = set()

        def de_quy(dinh):
            da_tham.add(dinh)

            # tô sáng đỉnh khi duyệt
            if dinh in do_thi["canvas_id"]:
                self.to_sang_dinh(do_thi["canvas_id"][dinh])

            # duyệt các đỉnh kề
            for ke in do_thi["ke"][dinh]:
                if ke not in da_tham:
                    de_quy(ke)

        de_quy(dinh_bat_dau)
        return da_tham
