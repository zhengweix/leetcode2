class Solution:
    def intersection(self, nums):
        intset = set(nums[0])
        for i in range(1, len(nums)):
            intset = intset & set(nums[i])

        return sorted(list(intset))
#1198