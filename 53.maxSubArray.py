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
    Maximum Product Subarray, Degree of an Array, Longest Turbulent Subarray, Maximum Score Of Spliced Array, Maximum Absolute Sum of Any Subarray, Maximum Subarray Sum After One Operation, Substring With Largest Variance, Count Subarrays With Score Less Than K
    '''
    def maxSubArray(self, nums):
        #* Kadane's algorithm, it defines an array s[] whose ith element represents the largest contiguous sum ending at nums[i]. Then, s[i+1] = max(s[i], 0) + nums[i]
        ans = sm = 0
        for num in nums:
            #* 0 is result of the empty s[]
            sm = max(0, sm+num)
            ans = max(ans, sm)
        return ans

    def maxSubArray1(self, nums):
        dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1])+nums[i]
        return max(dp)

    def main(self):
        print(self.maxSubArray1([-2,1,-3,4,-1,2,1,-5,4]))

S = Solution()
S.main()