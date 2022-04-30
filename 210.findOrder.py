class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        indeg = [0 for i in range(numCourses)]
        graph = defaultdict(list)
        for i, p in enumerate(prerequisites):
            graph[p[1]].append(p[0])
            indeg[p[0]] += 1

        sources = []
        for i in range(numCourses):
            if indeg[i] == 0:
                sources.append(i)

        while sources:
            u = sources.pop(0)
            order.append(u)
            for g in graph[u]:
                indeg[g] -= 1
                if indeg[g] == 0:
                    sources.append(g)

        if len(order) != numCourses:
            return []

        return order
