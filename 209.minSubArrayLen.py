from math import *
class Solution:
    '''
    Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

    Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

    Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

    Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104

    Follow up:
    If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

    Array, Binary Search, Sliding Window, Prefix Sum

    Minimum Window Substring, Maximum Size Subarray Sum Equals k, Maximum Length of Repeated Subarray, Minimum Operations to Reduce X to Zero, K Radius Subarray Averages, Maximum Product After K Increments
    '''

    def minSubArrayLen(self, target, nums):
        k = inf
        start, sm = 0, 0
        for end, num in enumerate(nums):
            sm += num
            while sm >= target:
                k = min(end - start + 1, k)
                sm -= nums[start]
                start += 1
        return k if k != inf else 0
    def main(self):
        print(self.minSubArrayLen(80, [10,5,13,4,8,4,5,11,14,9,16,10,20,8]))

S = Solution()
S.main()