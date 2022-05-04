from collections import *
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(string):
            d = defaultdict(lambda: [])
            for i, c in enumerate(string):
                d[c].append(i)
            return list(d.values())
        return helper(s) == helper(t)

#290