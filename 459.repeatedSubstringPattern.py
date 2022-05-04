class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        l1 = l//2
        for i in range(l1+1):
            p = s[:i+1]
            lp = len(p)
            if l%lp == 0 and l//lp > 1 and s.replace(p, '') == '':
                return True
        return False
#686