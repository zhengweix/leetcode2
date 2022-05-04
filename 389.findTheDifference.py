class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for c in s:
            xor = xor ^ ord(c)

        for c in t:
            xor = xor ^ ord(c)

        return chr(xor)
#1832 1087 2246