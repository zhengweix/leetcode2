class Solution:
    '''
    Given a string s, find the length of the longest substring without repeating characters.

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

    Next challenges:
    159 340 992 1695 2067 2260
    '''


























    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = {}
        k, start = 0, 0
        for end, c in enumerate(s):
            if c in ch:
                start = max(start, ch[c] + 1)
            ch[c] = end
            k = max(k, end - start + 1)
        return k