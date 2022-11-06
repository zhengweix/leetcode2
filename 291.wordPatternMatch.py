from collections import *
class Solution:
    '''
    Given a pattern and a string s, return true if s matches the pattern.
    A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

    Example 1:
    Input: pattern = "abab", s = "abab"
    Output: true
    Explanation: One possible mapping is as follows:
    'a' -> "red"
    'b' -> "blue"

    Example 2:
    Input: pattern = "aaaa", s = "asdasdasdasd"
    Output: true
    Explanation: One possible mapping is as follows:
    'a' -> "asd"

    Example 3:
    Input: pattern = "aabb", s = "xyzabcxzyabc"
    Output: false

    Constraints:
    1 <= pattern.length, s.length <= 20
    pattern and s consist of only lowercase English letters.

    Hash Table, String, Backtracking
    '''
    # tc:O(n*C(m, n)) sc: O(m + n)
    @staticmethod
    def wordPatternMatch(pattern, s):
        def helper(i, j):
            '''Return True if pattern[i:] can be mapping to s[j:]'''
            if i == len(pattern) and j == len(s):
                return True
            if i == len(pattern) or j == len(s):
                return False
            if pattern[i] in mp:
                if mp[pattern[i]] == s[j:j+len(mp[pattern[i]])] and helper(i+1, j+len(mp[pattern[i]])):
                    return True
                return False
            for k in range(j+1, len(s)+1):
                if s[j:k] in mp: # skip pre-stored non-workable segmentations
                    continue
                mp[pattern[i]] = s[j:k]
                mp[s[j:k]] = pattern[i]
                if helper(i+1, k):
                    return True
                mp.pop(pattern[i]) # store all possible non-workable segmentations
                if mp[pattern[i]] != s[j:k]:
                    mp.pop(s[j:k])
            return False
        mp = {}
        return helper(0, 0)

print(Solution.wordPatternMatch("ab", "aa"))