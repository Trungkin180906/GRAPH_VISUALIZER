# 5. KIỂM TRA ĐỒ THỊ 2 PHÍA (BIPARTITE)
def is_bipartite(adj):
    color = {}

    for start in adj:
        if start not in color:
            color[start] = 0
            q = deque([start])

            while q:
                u = q.popleft()
                for (v, _) in adj[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False

    return True