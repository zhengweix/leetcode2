class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i, n, dups = 0, len(nums), []
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i, n in enumerate(nums):
            if i+1 != n:
                dups.append(n)

        return dups
#2007 1424