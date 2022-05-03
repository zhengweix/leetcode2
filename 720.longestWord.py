class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda i: (-len(i), i))
        for i, word in enumerate(words):
            isbuilt = True
            for j in range(len(word)-1, 0, -1):
                if word[:j] not in words:
                    isbuilt = False
                    break
            if isbuilt:
                return word
            else:
                i += 1
        return ''
