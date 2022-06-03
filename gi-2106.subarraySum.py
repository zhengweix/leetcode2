class Solution:
    '''
    Given an array of integers nums and an integer k, return a subarray whose sum equals to k. If such a subset cannot be made, then return null.

    Input: nums = [12, 1, 61, 5, 9, 2], k = 24
    Output: [12, 9, 2, 1]
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        subsets, dp = [[]], defaultdict(list)
        for num in nums:
            if k - num in dp:
                return [num] + dp[k - num][0]
            for i in range(len(subsets)):
                set = list(subsets[i])
                set.append(num)
                subsets.append(set)
                dp[sum(set)].append(set)
        return None

