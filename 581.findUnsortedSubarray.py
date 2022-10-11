from math import *
class Solution:
    '''
    Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
    Return the shortest such subarray and output its length.

    Example 1:
    Input: nums = [2,6,4,8,10,9,15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

    Example 2:
    Input: nums = [1,2,3,4]
    Output: 0

    Example 3:
    Input: nums = [1]
    Output: 0

    Constraints:
    1 <= nums.length <= 104
    -105 <= nums[i] <= 105

    Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack

    To find the upper bound of the unsorted subarray, one needs to loop through the list forward and keep track of the running maximum.
    The last position where the element value doesn't match the running maximum is the upper bound (hi).
    Similarly, to find the lower bound, simply loop through the list backward (starting from hi), and the last position where the current element doens't match the running minimum marks the lower bound (lo).

    Max Increase to Keep City Skyline, Profitable Schemes, Meeting Rooms III
    '''
    def findUnsortedSubarray(self, nums):
        lo, hi = 0, len(nums)-1
        while lo < len(nums) - 1 and nums[lo+1] >= nums[lo]:
            lo += 1
        if lo == len(nums) - 1:
            return 0

        while hi > 0 and nums[hi-1] <= nums[hi]:
            hi -= 1

        mx, mn = -inf, inf
        for i in range(lo, hi+1):
            mx = max(nums[i], mx)
            mn = min(nums[i], mn)

        while lo > 0 and nums[lo-1] > mn:
            lo -= 1

        while hi < len(nums) - 1 and nums[hi+1] < mx:
            hi += 1

        return hi - lo + 1

    def findUnsortedSubarray1(self, nums):
        mn, mx = inf, -inf
        lo = hi = None
        for i in range(len(nums)):
            if nums[i] < (mx := max(mx, nums[i])):
                hi = i
            if nums[~i] > (mn := min(mn, nums[~i])):
                lo = len(nums) + ~i
        return hi - lo + 1 if hi else 0

    def main(self):
        print(self.findUnsortedSubarray1([1, 2, 5, 3, 7, 10, 9, 12]))

S = Solution()
S.main()