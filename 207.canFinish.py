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
            for u, v in prerequisites:
                if u == u:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        queue.append(v)
        return cnt == numCourses

    def canFinish1(self, numCourses, prerequisites):
        def helper(x):
            ''' detecting if cycle is detected. '''
            if seen[x]:
                return seen[x] == 1
            seen[x] = 1
            for u, v in prerequisites:
                if u == x and helper(v):
                        return True
            seen[x] = 2
            return False
        seen = [0] * numCourses
        for i in range(numCourses):
            if helper(i):
                return False
        return True

    def main(self):
        print(self.canFinish1(2, [[1,0], [0, 1]]))

S = Solution()
S.main()