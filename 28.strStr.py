class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        hy = haystack.replace(needle, "")
        if hy == haystack:
            return -1
        else:
            return haystack.index(needle)