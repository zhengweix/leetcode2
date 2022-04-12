class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dict = {}
        start, d, d_ = 0, 0, 0
        for end in range(len(s)):
            c = s[end]
            i = dict[c] if c in dict else 0
            i += 1
            dict[c] = i
            while len(dict) > k:
                c_ = s[start]
                i_ = dict[c_] - 1
                if i_ > 0:
                    dict[c_] = i_
                else:
                    del dict[c_]
                start += 1
                d = max(d, end - start + 1)
        return d