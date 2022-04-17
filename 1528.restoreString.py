class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ss = ''
        for i in range(len(s)):
            ss += s[indices.index(i)]

        return ss