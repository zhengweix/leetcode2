class Solution:
    def isHappy(self, n: int) -> bool:
        lst = []
        def helper(s):
            nonlocal lst
            sm = 0
            for d in str(s):
                sm += int(d) ** 2
            if sm == 1:
                return True
            elif sm in lst:
                return False
            else:
                if sm not in lst:
                    lst.append(sm)
                return helper(sm)
        return helper(n)