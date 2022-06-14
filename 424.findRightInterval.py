from collections import defaultdict
class Solution:
    '''
    You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.

    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length

    Next challenges:
    340 1004 2009 2024 2213
    '''






















    def characterReplacement(self, s: str, k: int) -> int:
        start, l, m = 0, 0, 0
        ch = defaultdict(int)
        for end, c in enumerate(s):
            ch[c] += 1
            m = max(m, ch[c])
            if end - start + 1 - m > k:
                ch[s[start]] -= 1
                start += 1

        return end - start + 1