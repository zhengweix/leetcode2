class Solution:
    '''
    Given an array of integers nums and an integer k, return a subarray whose sum equals to k. If such a subset cannot be made, then return null.

    Input: nums = [12, 1, 61, 5, 9, 2], k = 24
    Output: [12, 9, 2, 1]

    google
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [[[]]] + [[] for x in range(k)]
        for num in nums:


