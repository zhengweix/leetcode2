class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def helper(i, sum):
            nonlocal memo
            if (i, sum) in memo:
                return memo[(i, sum)]

            if i == l:
                if sum == target:
                    return 1
                return 0
            num = nums[i]
            memo[(i, sum)] = helper(i+1, sum+num) + helper(i+1, sum-num)
            return memo[(i, sum)]

        l = len(nums)
        return helper(0, 0)
#282