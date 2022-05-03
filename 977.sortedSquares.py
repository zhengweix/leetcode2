from collections import *
class Solution:
    def sortedSquares(self, nums):
        def helper(x):
            return x * x
        return list(map(helper, sorted(map(abs, nums))))

