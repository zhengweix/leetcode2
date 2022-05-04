class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dict = {}
        for i in range(10):
            dict[str(i)] = i

        n1, n2, d1, d2 = 0, 0, 0, 0
        for n in num1[::-1]:
            n1 += dict[n] * 10**d1
            d1 += 1

        for n in num2[::-1]:
            n2 += dict[n] * 10**d2
            d2 += 1

        return str(n1+n2)
#43 989