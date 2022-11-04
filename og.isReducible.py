class Solution:
    @staticmethod
    def isReducible(word, dictionary):
        def helper1(word1):
            if len(word1) == 1 and word1 in dictionary:
                return 1
            if word1 not in dictionary:
                return 0
            res = 0
            for i in range(len(word1)):
                res = res + helper1(word1[:i]+word1[i+1:])
            return res

        ans = False
        for i in range(len(word)):
            ans = ans + helper1(word[:i]+word[i+1:])
        return True if ans > 0 else False

print(Solution.isReducible('sprint', ['print', 'pint', 'pin', 'in', 'n']))