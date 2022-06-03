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
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1, count, cache = 0, 0, defaultdict(int)
        cache[0] += 1
        for num in nums:
            sum1 += num
            if sum1 - k in cache:
                count += cache[sum1 - k]
            cache[sum1] += 1
        return count


