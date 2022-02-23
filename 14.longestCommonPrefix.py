class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = 1
        prefix = ''
        m = len(strs[0])
        while n <= m:
            prefixLetter = ''
            for str in strs:
                if not str:
                    return ''

                if m > len(str):
                    m = len(str)
                if not prefixLetter:
                    prefixLetter = str[n - 1]
                else:
                    if prefixLetter != str[n - 1]:
                        return prefix

            prefix += prefixLetter
            n += 1

        return prefix

    def longestCommonPrefixOpt(self, strs: List[str]) -> str:
        n = 0
        prefix = ''
        m = len(min(strs))
        while True and n < m:
            for str in strs:
                if strs[0][n] != str[n]:
                    return prefix
            prefix += strs[0][n]
            n += 1
        return prefix