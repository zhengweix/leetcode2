from collections import *
class Solution:
    '''
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

    Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

    Example 2:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

    Example 3:
    Input: numCourses = 1, prerequisites = []
    Output: [0]

    Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    All the pairs [ai, bi] are distinct.

    Related Topics:
    Depth-First Search, Breadth-First Search, Graph, Topological Sort

    Next challenges:
    Course Schedule, Alien Dictionary, Minimum Height Trees, Sequence Reconstruction, Course Schedule III, Parallel Courses, Find All Possible Recipes from Given Supplies, Build a Matrix With Conditions

    turo
    '''
    #? keywords: prerequisites, one way ordering, empty array, bi -> ai
    #? approach: consider course/vertices and prerequisites/edges as graph, topological sort
    def findOrder1(self, numCourses, prerequisites):
        # input: numCourses 4
        #        prerequisites [[1,0],[2,0],[3,1],[3,2]]
        # output: [0,2,1,3]
        #? any course has no prerequisite
        indeg = [0 for i in range(numCourses)] # [0,0,0,0]
        #? go through prerequisites, compute indeg of v
        for pair in prerequisites:
            indeg[pair[0]] += 1
        # indeg = [0,1,1,2]
        #? store all coures having no prerequisite
        queue = []
        for u in range(numCourses):
            if indeg[u] == 0:
                queue.append(u)
        # queue = [0]
        ans = []
        #? to find new couses have no prerequite
        while queue:
            u = queue.pop(0) # 0,1,2
            ans.append(u) # [0],[0,1],[0,1,2]
            for pair in prerequisites:
                v1, u1 = pair[0], pair[1]
                if u1 == u:
                    #? course v1's num of prerequisites decreased by 1
                    indeg[v1] -= 1
                    if indeg[v1] == 0:
                        queue.append(v1)
        # queue = [1, 2],[2],[3]
        # indeg = [0,0,0,2],[0,0,0,1],[0,0,0,0]
        return ans

    def main(self):
        print(self.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

S = Solution()
S.main()