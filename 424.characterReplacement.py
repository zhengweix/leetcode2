class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, l, m = 0, 0, 0
        ch = collections.defaultdict(int)
        for end, c in enumerate(s):
            ch[c] += 1
            m = max(m, ch[c])
            if end - start + 1 - m > k:
                ch[s[start]] -= 1
                start += 1

        return end - start + 1