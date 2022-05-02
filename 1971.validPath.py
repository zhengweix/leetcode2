from collections import *
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        queue = [source]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = []
        while queue:
            node = queue.pop(0)
            visited.append(node)
            if node == destination:
                return True
            for v in graph[node]:
                if v not in visited:
                    queue.append(v)

        return False
