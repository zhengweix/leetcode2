from collections import *
class Solution:
    '''
    Given a pattern and a string s, return true if s matches the pattern.
    A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

    Example 1:
    Input: pattern = "abab", s = "redblueredblue"
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
    @staticmethod
    def wordPatternMatch(pattern, s):
        def helper(s1, pattern1, mp):
            if not pattern1:
                return s1 == ''

            p = pattern[0]
            for i in range(1, len(s1)+1):
                if (mp[p] and s1[:i] == mp[p]) or not mp[p]:
                    mp[p] = s1[:i]
                    if not helper(s1[i:], pattern1[1:], mp):
                        if mp[p]:
                            del mp[p]

        return helper(s, pattern, defaultdict(str))

print(Solution.wordPatternMatch("aaaa", "asdasdasdasd"))