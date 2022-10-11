from bisect import *
class Solution:
    '''
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

    Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

    Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
    '''
    def searchRange(self, nums, target):
        #* Use self-implemented bisect_left and bisect_right to identify the left and right boundaries of the range.
        def helper():
            # bisection search (left most boundary)
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + hi >> 1
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def helper1():
            # bisection search (right most boundary)
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + hi >> 1
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = helper()
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        return [lo, helper1() - 1]

    def main(self):
        print(self.searchRange([5,7,7,8,8,10], 8))

S = Solution()
S.main()




