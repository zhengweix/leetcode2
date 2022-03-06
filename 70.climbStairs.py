from functools import lru_cache
class Solution:
    @lru_cache(1000)
    def fibonacci(self, n: int) -> int:
        return 1 if n < 2 else self.fibonacci(n - 2) + self.fibonacci(n - 1)

    def climbStairs(self, n: int) -> int:
        return self.fibonacci(n)