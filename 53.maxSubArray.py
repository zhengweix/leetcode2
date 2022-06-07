class Solution:
    '''
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

    Input: nums = [1]
    Output: 1

    Input: nums = [5,4,-1,7,8]
    Output: 23

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

    Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

    Next challenges:
    152 697 978 1749 1746 2272
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        sum1, sum2 = nums[0], 0
        for num in nums:
            if sum2 < 0:
                sum2 = num
            else:
                sum2 += num
            sum1 = max(sum1, sum2)
        return sum1
