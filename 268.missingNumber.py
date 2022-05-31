class Solution:
    '''
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
    '''
    def missingNumber(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]
            if j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i, num in enumerate(nums):
            if i != num:
                return i

        return n

    def missingNumber2(self, nums: List[int]) -> int:
        n, x1 = len(nums), 0
        for i in range(1, n + 1):
            x1 = x1 ^ i
        x2 = nums[0]
        for j in range(1, n):
            x2 = x2 ^ nums[j]

        return x1 ^ x2
#287 1980 41 765