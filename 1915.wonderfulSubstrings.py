from collections import *
class Solution:
    '''
     wonderful string is a string where at most one letter appears an odd number of times.
    For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
    Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.
    A substring is a contiguous sequence of characters in a string.

    Example 1:
    Input: word = "aba"
    Output: 4
    Explanation: The four wonderful substrings are underlined below:
    - "aba" -> "a"
    - "aba" -> "b"
    - "aba" -> "a"
    - "aba" -> "aba"

    Example 2:
    Input: word = "aabb"
    Output: 9
    Explanation: The nine wonderful substrings are underlined below:
    - "aabb" -> "a"
    - "aabb" -> "aa"
    - "aabb" -> "aab"
    - "aabb" -> "aabb"
    - "aabb" -> "a"
    - "aabb" -> "abb"
    - "aabb" -> "b"
    - "aabb" -> "bb"
    - "aabb" -> "b"

    Example 3:
    Input: word = "he"
    Output: 2
    Explanation: The two wonderful substrings are underlined below:
    - "he" -> "h"
    - "he" -> "e"

    Constraints:
    1 <= word.length <= 105
    word consists of lowercase English letters from 'a' to 'j'.

    Hash Table, String, Bit Manipulation, Prefix Sum

    Prefix and Suffix Search, Simplified Fractions, Simple Bank System
    '''
    #! Time Limit Exceeded sc: O(n^2)
    def wonderfulSubstrings(self, word):
        def helper(s):
            return sum(True if v % 2 == 1 else False for v in dict(Counter(s)).values()) <= 1

        ans = 0
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                ans += helper(word[i:j])
        return ans

    #https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1300877/Python-O(n)-solution-with-comments-Prefix-sum-bit-mask
    def wonderfulSubstrings1(self, word):
        ans = mask = 0
        freq = defaultdict(int, {0: 1})
        for ch in word:
            mask ^= 1 << ord(ch) - 97
            ans += freq[mask]
            for i in range(10):
                ans += freq[mask ^ 1 << i]
            freq[mask] += 1
        return ans

def main(self):
        print(self.wonderfulSubstrings("aba"))

S = Solution()
S.main()