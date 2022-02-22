class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalindrome = True
        stringx = str(x)
        arrayx = [i for i in stringx]
        string = ''
        for i in range(len(arrayx)-1, -1, -1):
            string += arrayx[i]

        if string != stringx:
            isPalindrome = False

        return isPalindrome

    def isPalindromeInt(self, x: int) -> bool:
        if x != abs(x):
            return False

        stringx = str(x)
        arrayx = [int(i) for i in stringx]
        n = len(arrayx)
        isPalindrome = True
        for i in range(n):
            if arrayx[i] != arrayx[n-1-i]:
                isPalindrome = False
                break

        return isPalindrome