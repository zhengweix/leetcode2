from collections import *
class Solution:
    '''
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

    Example 1:
    Input: s = "leetcode"
    Output: 0

    Example 2:
    Input: s = "loveleetcode"
    Output: 2

    Example 3:
    Input: s = "aabb"
    Output: -1

    Constraints:
    1 <= s.length <= 105
    s consists of only lowercase English letters.

    Hash Table, String, Queue, Counting

    Sort Characters By Frequency, First Letter to Appear Twice
    #451
    '''
    def firstUniqChar(self, s):
        return next((i for i, c in enumerate(s) if s.index(c) == s.rindex(c)), -1)
    def firstUniqChar1(self, s):
        freq = Counter([*s])
        return next((i for i, c in enumerate(s) if freq[c] == 1), -1)
    def firstUniqChar2(self, s):
        freq = {}
        for c in s: freq[c] = 1 + freq.get(c, 0)
        return next((i for i, c in enumerate(s) if freq[c] == 1), -1)