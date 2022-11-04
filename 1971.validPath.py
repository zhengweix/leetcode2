from collections import *
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt != qrt:
            self.parent[qrt] = prt

class Solution:
    '''
    There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
    You want to determine if there is a valid path that exists from vertex source to vertex destination.
    Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

    Example 1:
    https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    Explanation: There are two paths from vertex 0 to vertex 2:
    - 0 → 1 → 2
    - 0 → 2

    Example 2:
    https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png
    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
    Explanation: There is no path from vertex 0 to vertex 5.

    Constraints:
    1 <= n <= 2 * 105
    0 <= edges.length <= 2 * 105
    edges[i].length == 2
    0 <= ui, vi <= n - 1
    ui != vi
    0 <= source, destination <= n - 1
    There are no duplicate edges.
    There are no self edges.

    Depth-First Search, Breadth-First Search, Union Find, Graph

    Valid Arrangement of Pairs
    Paths in Maze That Lead to Same Room
    '''
    @staticmethod
    def validPath(n, edges, source, destination):
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

    @staticmethod
    # tc: O(mlogn) where m is num of edges, sc: O(n)
    def validPath1(n, edges, source, destination):
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.find(source) == ut.find(destination)

print(Solution.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))