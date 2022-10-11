from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        assert n > 0
        self.n = n
        self.parent = [i for i in range(n)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        '''Unite the two elements by uniting their parents.'''
        xparent, yparent = self.find(x), self.find(y)
        if xparent != yparent:
            self.parent[yparent] = xparent

class Solution:
    '''
    Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.

    Example
    For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
    solution(str, pairs) = "dbca".

    By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".

    Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string str
    A string consisting only of lowercase English letters.
    Guaranteed constraints:
    1 ≤ str.length ≤ 104.
    [input] array.array.integer pairs
    An array containing pairs of indices that can be swapped in str (1-based). This means that for each pairs[i], you can swap elements in str that have the indices pairs[i][0] and pairs[i][1].å

    Guaranteed constraints:
    0 ≤ pairs.length ≤ 5000,
    pairs[i].length = 2.

    [output] string
    '''
    def swapLexOrder(self, s, pairs):
        s = list(s)
        uf = UnionFind(len(s))
        for u, v in pairs:
            uf.union(u - 1, v - 1)
        mp = defaultdict(list)
        for n in range(len(s)):
            mp[uf.find(n)].append(n)
        for path in mp.values():
            for i, c in zip(sorted(path, reverse=True), sorted([s[i] for i in path])):
                s[i] = c
        return ''.join(s)

    def main(self):
        print(self.swapLexOrder("abdc", [[1, 4], [3, 4]]))

S = Solution()
S.main()