class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n, x = len(nums), nums[0]
        for i in range(1, n):
            x = x ^ nums[i]

        return x