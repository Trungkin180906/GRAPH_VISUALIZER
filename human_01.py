import json
def save_graph(node, edges, filename="Graph_data.json"):
    data={"nodes":node, "edges":edges}#tạo dict 
    with open(filename, 'w')as f:#mở file ở chế độ write 
        json.dump(data, f)#lưu dữ liệu thành file json
    print("Đã lưu đồ thị thành công")

def load_graph(filename="Graph_data.json"):
    try:
        with open(filename, 'r') as f:#mở filr ở chế độ đọc
            data=json.load(f)#chuyển nội dung json sang dict python
            return data["nodes"], data["edges"]
    except FileNotFoundError:
        return [], []#trả về rỗng nếu chưa có file
    
