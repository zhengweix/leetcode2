from collections import defaultdict
from unionFind import UnionFind
class Solution:
    '''
    You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
    You can swap the characters at any pair of indices in the given pairs any number of times.
    Return the lexicographically smallest string that s can be changed to after using the swaps.

    Example 1:
    Input: s = "dcab", pairs = [[0,3],[1,2]]
    Output: "bacd"
    Explaination:
    Swap s[0] and s[3], s = "bcad"
    Swap s[1] and s[2], s = "bacd"

    Example 2:
    Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
    Output: "abcd"
    Explaination:
    Swap s[0] and s[3], s = "bcad"
    Swap s[0] and s[2], s = "acbd"
    Swap s[1] and s[2], s = "abcd"

    Example 3:
    Input: s = "cba", pairs = [[0,1],[1,2]]
    Output: "abc"
    Explaination:
    Swap s[0] and s[1], s = "bca"
    Swap s[1] and s[2], s = "bac"
    Swap s[0] and s[1], s = "abc"

    Constraints:
    1 <= s.length <= 10^5
    0 <= pairs.length <= 10^5
    0 <= pairs[i][0], pairs[i][1] < s.length
    s only contains lower case English letters.

    Hash Table, String, Depth-First Search, Breadth-First Search, Union Find

    Minimize Hamming Distance After Swap Operations, Process Restricted Friend Requests, Largest Number After Digit Swaps by Parity
    '''
    def smallestStringWithSwaps(self, s, pairs):
        '''BFS createa directed graph first and then get all the connected components.'''
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        seen, mp = set(), []
        def helper(u):
            path, queue = [], [u]
            seen.add(u)
            while queue:
                u = queue.pop(0)
                path.append(u)
                for v in graph[u]:
                    if v not in seen:
                        queue.append(v)
                        seen.add(v)
            return path
        n = len(s)
        for i in range(n):
            if i not in seen:
                mp.append(helper(i))

        ans = {}
        for path in mp:
            for i, c in zip(sorted(path), sorted(s[i] for i in path)):
                ans[i] = c
        return ''.join(ans[i] for i in range(n))

    def smallestStringWithSwaps1(self, s, pairs):
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        seen, mp = set(), defaultdict(list)
        def helper(u, i):
            mp[i].append(u)
            seen.add(u)
            for v in graph[u]:
                if v not in seen:
                    helper(v, i)

        n, idx = len(s), 0
        for i in range(n):
            if i not in seen:
                helper(i, idx)
                idx += 1

        ans = {}
        for path in mp.values():
            for i, c in zip(sorted(path), sorted(s[i] for i in path)):
                ans[i] = c
        return ''.join(ans[i] for i in range(n))

    def smallestStringWithSwaps2(self, s, pairs):
        '''union-find'''
        s = list(s)
        uf = UnionFind(len(s))
        for u, v in pairs:
            uf.union(u, v)
        mp = defaultdict(list)
        for n in range(len(s)):
            mp[uf.find(n)].append(n)
        for path in mp.values():
            for i, c in zip(sorted(path), sorted([s[i] for i in path])):
                s[i] = c
        return ''.join(s)

    def main(self):
        print(self.smallestStringWithSwaps2("abdc", [[0,3], [2,3]]))

S = Solution()
S.main()