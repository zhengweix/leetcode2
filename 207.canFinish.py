class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0 for i in range(numCourses)]
        for i, e in enumerate(prerequisites):
            graph[e[0]].append(e[1])
            indeg[e[1]] += 1

        sources, order = [], []
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

        return len(order) == numCourses