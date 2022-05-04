class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return log(n)/log(4) == int(log(n)/log(4))
