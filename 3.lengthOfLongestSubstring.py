class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = {}
        k, start = 0, 0
        for end, c in enumerate(s):
            if c in ch:
                start = max(start, ch[c] + 1)
            ch[c] = end
            k = max(k, end - start + 1)
        return k