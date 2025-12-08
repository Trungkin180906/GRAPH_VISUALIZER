# 4. BFS + DFS 
def bfs(start, adj, node_pos, gui):
    print("\n--- BFS ---")

    visited = set()
    q = deque([start])

    order = []

    while q:
        u = q.popleft()
        if u not in visited:
            visited.add(u)
            order.append(u)

            x, y = node_pos[u]
            gui.highlight_node(x, y, u)

            for (v, _) in adj[u]:
                if v not in visited:
                    q.append(v)

    print("BFS order:", order)
    return order


def dfs(start, adj, node_pos, gui):
    print("\n--- DFS ---")

    visited = set()
    order = []

    def dfs_visit(u):
        visited.add(u)
        order.append(u)

        x, y = node_pos[u]
        gui.highlight_node(x, y, u)

        for (v, _) in adj[u]:
            if v not in visited:
                dfs_visit(v)

    dfs_visit(start)
    print("DFS order:", order)
    return order