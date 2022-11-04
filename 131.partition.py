class Solution:
    '''
    Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

    A palindrome string is a string that reads the same backward as forward.

    Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

    Example 2:
    Input: s = "a"
    Output: [["a"]]

    Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.

    String, Dynamic Programming, Backtracking

    Palindrome Partitioning II
    Palindrome Partitioning IV
    '''
    @staticmethod
    def partition(s):
        def helper(s1, ans, path): # dfs backtracking
            if not s1:
                ans.append(path)
                return
            for i in range(1, len(s1)+1):
                print(s1[:i])
                if s1[:i] == s1[i-1::-1]:
                    helper(s1[i:], ans, path+[s1[:i]])

        ans = []
        helper(s, ans, [])
        return ans

print(Solution.partition('aab'))








