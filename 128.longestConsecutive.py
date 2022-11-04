class Solution:
    '''
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.

    Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

    Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9


    Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109

    Array, Hash Table, Union Find

    Binary Tree Longest Consecutive Sequence
    Find Three Consecutive Integers That Sum to a Given Number
    Maximum Consecutive Floors Without Special Floors
    Length of the Longest Alphabetical Continuous Substring
    '''
    # sliding window tc: O(nlogn)
    @staticmethod
    def longestConsecutive(nums):
        ans, start = 0, 0
        nums = sorted(set(nums))
        for end, x in enumerate(nums):
            if end > 0 and x - nums[end - 1] > 1:
                start = end
            ans = max(ans, end - start + 1)
        return ans
    # union find tc: O(n)
    @staticmethod
    def longestConsecutive1(nums):
        ans, nums = 0, set(nums) # reducing duplicate check
        for x in nums:
            if x-1 not in nums: # reducing duplicate check
                xx = x + 1
                while xx in nums:
                    xx += 1
                ans = max(ans, xx - x)
        return ans

    @staticmethod
    def longestConsecutive2(nums):
        '''use a dictionary lcs to keep track of the length of the longest consequtive sequence it is in. Apparently, it takes O(n^2) to update all elements. Instead, it is enough to only update such info through boundary elements.'''
        lcs = dict()
        for x in nums:
            if x not in lcs:
                lcs[x] = lcs[x + lcs.get(x + 1, 0)] = lcs[x - lcs.get(x - 1, 0)] = 1 + lcs.get(x + 1, 0) + lcs.get(
                    x - 1, 0)
        return max(lcs.values(), default=0)

print(Solution.longestConsecutive1([100,4,200,1,3,2]))

