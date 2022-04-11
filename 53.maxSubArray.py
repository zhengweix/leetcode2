class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumx, sum_ = nums[0], 0
        for num in nums:
            if sum_ < 0:
                sum_ = num
            else:
                sum_ += num

            sumx = max(sumx, sum_)

        return sumx
