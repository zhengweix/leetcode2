from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start, match = 0, 0
        ch = defaultdict(int)
        n = len(s1)
        for c in s1:
            ch[c] += 1

        for end, c in enumerate(s2):
            if c in ch:
                ch[c] -= 1
                if ch[c] == 0:
                    match += 1

            if match == len(ch):
                return True

            if end >= n - 1:
                cc = s2[start]
                start += 1
                if cc in ch:
                    if ch[cc] == 0:
                        match -= 1
                    ch[cc] += 1

        return False