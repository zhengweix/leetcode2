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
    '''
    def canPartition(self, nums: List[int]) -> bool:
        sum1 = sum(nums)
        if sum1 % 2:
            return False
        len1 = len(nums)
        target = sum1 // 2
        dp = [[False for y in range(target + 1)] for x in range(len1)]
        for i in range(len1):
            dp[i][0] = True
        for j in range(1, target + 1):
            dp[0][j] = j == nums[0]
        for i in range(1, len1):
            for j in range(1, target + 1):
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif j > nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]
        return dp[len1 - 1][target]

    def canPartition1(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for current in nums:
            for new_target in range(target, current - 1, -1):
                dp[new_target] = dp[new_target] or dp[new_target - current]
        return dp[target]