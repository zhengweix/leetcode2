import sys
class Solution:
    '''
    You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.
    You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
    Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

    Example 1:
    https://assets.leetcode.com/uploads/2021/07/17/graph2.png
    Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    Output: 4
    Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
    The four ways to get there in 7 minutes are:
    - 0 ➝ 6
    - 0 ➝ 4 ➝ 6
    - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
    - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

    Example 2:
    Input: n = 2, roads = [[1,0,10]]
    Output: 1
    Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

    Constraints:
    1 <= n <= 200
    n - 1 <= roads.length <= n * (n - 1) / 2
    roads[i].length == 3
    0 <= ui, vi <= n - 1
    1 <= timei <= 109
    ui != vi
    There is at most one road connecting any two intersections.
    You can reach any intersection from any other intersection.

    Next Challenges:
    All Paths From Source to Target, Path with Maximum Probability, Second Minimum Time to Reach Destination
    '''
    def countPaths(self, n: int, roads):
        graph = {}
        for u, v, time in roads:
            graph.setdefault(u, {})[v] = time
            graph.setdefault(v, {})[u] = time
        dist = [sys.maxsize] * n
        dist[-1] = 0
        stack = [(n-1, 0)]
        while stack:
            u, t = stack.pop()
            #!
            if t == dist[u]:
                for v in graph.get(u, {}):
                    if t + graph[u][v] < dist[v]:
                        dist[v] = t + graph[u][v]
                        stack.append((v, t + graph[u][v]))

        def helper(u):
            if u == n-1:
                return 1
            if dist[u] == sys.maxsize:
                return 0
            ans = 0
            for v in graph.get(u, {}):
                if graph[u][v] + dist[v] == dist[u]:
                    ans += helper(v)
            return ans % 1_000_000_007

        return helper(0)

    def main(self):
        print(self.countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))


S = Solution()
S.main()