class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i, c in enumerate(s):
            if c in dict:
                dict[c][1] += 1
            else:
                dict[c] = [i, 1]

        for c in s:
            if dict[c][1] == 1:
                return dict[c][0]
        return -1
#451

