from collections import *
class Solution:
    '''
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
    A subarray is a contiguous non-empty sequence of elements within an array.

    Input: nums = [1,1,1], k = 2
    Output: 2

    Input: nums = [1,2,3], k = 3
    Output: 2

    Input: nums = [1, 2, 7, 1, 5], k = 9
    Output: 1 ([2, 7])

    Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107

    Array, Hash Table, Prefix Sum

    Next challenges:
    523 713 974 1658 2090 2219
    Continuous Subarray Sum, Subarray Sums Divisible by K, Minimum Operations to Reduce X to Zero, K Radius Subarray Averages, Maximum Sum Score of Array
    '''
    def subarraySum(self, nums, k):
        # if we save the sm in a cache and check if we've visited an index where the prefix sum was pref - k,
        # we know that we have an ending point to a subarray that equals to k.
        pref, ans, dp = 0, 0, defaultdict(int, {0:1})
        for x in nums:
            pref += x
            ans += dp[pref - k]
            dp[pref] += 1
        return ans

    def main(self):
        print(self.subarraySum([1, 2, 7, 1, 5], 9))

S = Solution()
S.main()


