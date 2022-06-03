class Solution:
    '''
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
    A subarray is a contiguous non-empty sequence of elements within an array.

    Input: nums = [1,1,1], k = 2
    Output: 2

    Input: nums = [1,2,3], k = 3
    Output: 2

    Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107

    Next challenges:
    523 713 974 1658 2090 2219
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        if we save the sum1 in a cache and check if we've visited an index where the sum1' was sum1 - k, we know that we have an ending point to a subarray that equals to k.
        '''
        sum1, count, dp = 0, 0, defaultdict(int, {0: 1})
        for num in nums:
            sum1 += num
            count += dp[sum1 - k]
            dp[sum1] += 1
        return count


