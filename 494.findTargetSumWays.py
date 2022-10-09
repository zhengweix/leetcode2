from functools import *
class Solution:
    '''
    You are given an integer array nums and an integer target.
    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
    Return the number of different expressions that you can build, which evaluates to target.

    Example 1:
    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3

    Example 2:
    Input: nums = [1], target = 1
    Output: 1

    Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000

    Array, Dynamic Programming, Backtracking
    #282 Expression Add Operators
    '''
    def findTargetSumWays(self, nums, target):
        @lru_cache(None)
        def helper(i, sm):
            if i == len(nums):
                return sm == target
            return helper(i+1, sm+nums[i]) + helper(i+1, sm-nums[i])
        return helper(0, 0)

    def findTargetSumWays1(self, nums, target):
        dp = [[0]*(target+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = 1

        for j in range(1, target+1):
            dp[0][j] = int(nums[0] == j)

        for y in range(1, len(nums)):
            for x in range(1, target+1):
                dp[y][x] = dp[y-1][x]
                if x >= nums[y-1]:
                    dp[y][x] += dp[y-1][x-nums[y-1]]
        return dp[len(nums)-1][target]
    def main(self):
        print(self.findTargetSumWays1([1, 1, 1, 1, 1], 1))

S = Solution()
S.main()