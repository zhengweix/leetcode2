class Solution:
    '''
    Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

    Example 1:
    Input: nums = [10,5,2,6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are:
    [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

    Example 2:
    Input: nums = [1,2,3], k = 0
    Output: 0

    Constraints:
    1 <= nums.length <= 3 * 104
    1 <= nums[i] <= 1000
    0 <= k <= 106

    Similar Questions
    Maximum Product Subarray, Maximum Size Subarray Sum Equals k, Medium, Subarray Sum Equals K, Two Sum Less Than K, Number of Smooth Descent Periods of a Stock, Count Subarrays With Score Less Than K
    '''
    # tc: O(n^2) sc: O(1)
    def numSubarrayProductLessThanK(self, nums, k):
        ans, lo, prod = 0, 0, 1
        for hi in range(len(nums)):
            prod *= nums[hi]
            while lo <= hi and prod >= k:
                prod /= nums[lo]
                lo += 1
            ans += hi - lo + 1
        return ans

    def main(self):
        print(self.numSubarrayProductLessThanK([10,5,2,6], 100))

S = Solution()
S.main()