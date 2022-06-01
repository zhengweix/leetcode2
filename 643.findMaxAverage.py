class Solution:
    '''
    You are given an integer array nums consisting of n elements, and an integer k.
    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

    Input: nums = [5], k = 1
    Output: 5.00000

    Constraints:
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104
    '''
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = -sys.maxsize;
        winSum, winStart = 0.0, 0
        for i in range(len(nums)):
            winSum += nums[i]
            if i >= k - 1:
                result = max(result, winSum / k)
                winSum -= nums[winStart]
                winStart += 1

        return result