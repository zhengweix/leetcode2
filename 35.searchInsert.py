class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            mid = nums[m]
            if mid == target:
                return m
            elif mid > target:
                r = m - 1
            else:
                l = m + 1

        return l