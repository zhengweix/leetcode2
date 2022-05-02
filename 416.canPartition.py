class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s, l = s // 2, len(nums)
        dp = [[False for x in range(s + 1)] for y in range(l)]
        for i in range(l):
            dp[i][0] = True

        for j in range(1, s + 1):
            dp[0][j] = nums[0] == j

        for i in range(1, l):
            for j in range(1, s + 1):
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]

        return dp[l - 1][s]
