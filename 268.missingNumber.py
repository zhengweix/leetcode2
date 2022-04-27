class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x1 = 0
        for i in range(1, n + 1):
            x1 = x1 ^ i

        x2 = nums[0]
        for j in range(1, n):
            x2 = x2 ^ nums[j]

        return x1 ^ x2