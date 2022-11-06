from itertools import *
class Solution:
    '''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]

    Constraints:
    1 <= n <= 8

    String, Dynamic Programming, Backtracking

    2116. Check if a Parentheses String Can Be Valid
    '''
    # tc: O(n^2) sc: O(n)
    @staticmethod
    def generateParenthesis(n):
        def helper(s):
            op, cl = 0, 0
            for c in s:
                if c == '(':
                    op += 1
                else:
                    cl += 1
                if op < cl:
                    return False
            return op == n and cl == n
        ans = []
        for s in set([''.join(x) for x in product('()', repeat=2*n)]):
            if helper(s):
                ans.append(s)
        return ans

    # tc: O(4^n/n^1.5) sc: O(4^n/n^1.5)
    # https://en.wikipedia.org/wiki/Catalan_number
    @staticmethod
    def generateParenthesis1(n):
        '''Backtracking to collect parentheses'''
        def helper(s, op, cl):
            if cl == n:
                ans.append(s)
            if op < n:
                helper(s+'(', op+1, cl)
            if cl < op:
                helper(s+')', op, cl+1)

        ans = []
        helper('', 0, 0)
        return ans

    @staticmethod
    def generateParenthesis2(n):
        ans = [['']]
        for i in range(1, n+1):
            tmp = []
            for j in range(i):
                for k in ans[j]:
                    for l in ans[~j]:
                        tmp.append(f"({k}){l}")
            ans.append(tmp)
        return ans[-1]

print(Solution.generateParenthesis2(3))