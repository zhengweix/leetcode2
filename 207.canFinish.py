class Solution:
    '''
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.

    Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

    Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

    Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.

    Depth-First Search, Breadth-First Search, Graph, Topological Sort

    Graph Valid Tree, Minimum Height Trees, Course Schedule III, Build a Matrix With Conditions
    '''
    def canFinish(self, numCourses, prerequisites):
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

    def canFinish1(self, numCourses, prerequisites):
        indeg = [0] * numCourses
        for p in prerequisites:
            indeg[p[1]] += 1

        cnt, queue = 0, []
        for i, deg in enumerate(indeg):
            if deg == 0:
                queue.append(i)

        while queue:
            u = queue.pop(0)
            cnt += 1
            for p in prerequisites:
                if p[0] == u:
                    indeg[p[1]] -= 1
                    if indeg[p[1]] == 0:
                        queue.append(p[1])
        return cnt == numCourses

    def main(self):
        print(self.canFinish1(2, [[1,0], [0, 1]]))

S = Solution()
S.main()