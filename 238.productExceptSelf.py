class Solution:
    '''
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

    Next challenges:
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, zeros, prod = [], [], 1
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
            else:
                prod = prod * num
        len1, len2 = len(nums), len(zeros)
        for i, num in enumerate(nums):
            if len2 > 1:
                return [0 for i in range(len1)]
            elif len2 == 1:
                if i == zeros[0]:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                prod1 = prod
                res.append(prod1//num)
        return res