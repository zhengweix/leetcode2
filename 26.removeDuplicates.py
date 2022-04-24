class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 1, 1
        while i < n:
            if nums[j - 1] != nums[i]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j