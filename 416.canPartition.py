from functools import *
class Solution:
    '''
    Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.

    Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 100

    Next challenges:
    698 1981 2025 2035
    Partition to K Equal Sum Subsets, Minimize the Difference Between Target and Chosen Elements, Maximum Number of Ways to Partition an Array, Partition Array Into Two Arrays to Minimize Sum Difference, Find Subarrays With Equal Sum
    '''
    def canPartition(self, nums):
        if (sm := sum(nums)) % 2:
            return False
        target = sm // 2
        dp = [0] * (target + 1)
        dp[0] = True
        for x in nums:
            for t in range(target, current - 1, -1):
                dp[t] = dp[t] or dp[t - x]
        return dp[target]

    def canPartition1(self, nums):
        if (sm := sum(nums)) % 2:
            return False
        @lru_cache(None)
        def helper(i, tar):
            if tar <= 0:
                return tar == 0
            if i == len(nums):
                return False
            return helper(i+1, tar-nums[i]) or helper(i+1, tar)
        return helper(0, sm//2)

    def canPartition2(self, nums):
        if (sm := sum(nums)) % 2:
            return False
        bits = 1
        for x in nums:
            bits |= bits << x
        return bool(bits & (1 << sm // 2))


    def main(self):
        print(self.canPartition1([1, 2, 5]))

S = Solution()
S.main()