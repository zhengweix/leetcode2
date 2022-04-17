class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dict = {}
        start, d, d_ = 0, 0, 0
        for end, c in enumerate(s):
            c = s[end]
            i = dict[c] if c in dict else 0
            i += 1
            dict[c] = i
            while len(dict) > k:
                c_ = s[start]
                dict[c_] -= 1
                if dict[c_] == 0:
                    del dict[c_]
                start += 1
            d = max(d, end - start + 1)
        return d