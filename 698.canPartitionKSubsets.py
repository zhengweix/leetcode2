class Solution:
    '''
    Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

    Example 1:
    Input: nums = [4,3,2,3,5,2,1], k = 4
    Output: true
    Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

    Example 2:
    Input: nums = [1,2,3,4], k = 3
    Output: false

    Constraints:
    1 <= k <= nums.length <= 16
    1 <= nums[i] <= 104
    The frequency of each element is in the range [1, 4].

    2305. Fair Distribution of Cookies
    2025. Maximum Number of Ways to Partition an Array
    2397. Maximum Rows Covered by Columns
    '''
    @staticmethod
    def canPartitionKSubsets(nums, k):
        if sum(nums) % k:
            return False
        avg = sum(nums) // k
        sm = [0]*k
        nums.sort(reverse=True) # avoiding Time Limit Exceeded

        def helper(i):
            if i == len(nums):
                return True

            for kk in range(k):
                if sm[kk] + nums[i] <= avg:
                    sm[kk] += nums[i]
                    if helper(i+1):
                        return True
                    sm[kk] -= nums[i]
                if sm[kk] == 0:
                    break
            return False
        return helper(0)

print(Solution.canPartitionKSubsets([1,2,3,4], 3))