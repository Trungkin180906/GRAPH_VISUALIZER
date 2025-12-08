# 6. CHUYỂN ĐỔI GIỮA MA TRẬN / DANH SÁCH / DANH SÁCH CẠNH
# # Ma trận kề
def adj_list_to_matrix(adj):
    nodes = list(adj.keys())
    n = len(nodes)
    index = {nodes[i]: i for i in range(n)}

    matrix = [[0]*n for _ in range(n)]
    for u in adj:
        for (v, w) in adj[u]:
            matrix[index[u]][index[v]] = w

    return nodes, matrix


# Danh sách cạnh
def adj_list_to_edge_list(adj):
    edges = []
    for u in adj:
        for (v, w) in adj[u]:
            edges.append((u, v, w))
    return edges


# Chuyển ngược từ ma trận về danh sách kề
def matrix_to_adj_list(nodes, matrix):
    adj = {nodes[i]: [] for i in range(len(nodes))}

    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if matrix[i][j] != 0:
                adj[nodes[i]].append((nodes[j], matrix[i][j]))

    return adj
