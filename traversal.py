# traversal.py
from collections import deque

class GraphTraversal:
    """
    Module của người số 4: chứa BFS và DFS.
    - adj: dict {node: [neighbour1, neighbour2, ...]}
    - gui: đối tượng GUI có phương thức highlight(node_id) (tạm in ra)
    """

    def bfs(self, start, adj, gui=None):
        visited = set()
        q = deque([start])
        order = []

        while q:
            u = q.popleft()
            if u not in visited:
                visited.add(u)
                order.append(u)

                if gui:
                    # gọi GUI để highlight node (GUI sẽ implement effect sau)
                    gui.highlight(u)

                for v in adj.get(u, []):
                    if v not in visited:
                        q.append(v)

        return order

    def dfs(self, start, adj, gui=None):
        visited = set()
        order = []

        def _dfs(u):
            visited.add(u)
            order.append(u)

            if gui:
                gui.highlight(u)

            for v in adj.get(u, []):
                if v not in visited:
                    _dfs(v)

        _dfs(start)
        return order
