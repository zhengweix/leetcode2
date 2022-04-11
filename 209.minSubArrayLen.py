class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        k = 10 ** 5 + 1
        sum_, start = 0, 0
        for end in range(len(nums)):
            sum_ += nums[end]
            while sum_ >= target:
                k = min(k, end - start + 1)
                sum_ -= nums[start]
                start += 1

        if k == 10 ** 5 + 1:
            return 0
        return k