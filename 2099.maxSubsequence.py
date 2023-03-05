from itertools import combinations
from heapq import *
class Solution:
    '''
    You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
    Return any such subsequence as an integer array of length k.
    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

    Example 1:
    Input: nums = [2,1,3,3], k = 2
    Output: [3,3]
    Explanation:
    The subsequence has the largest sum of 3 + 3 = 6.

    Example 2:
    Input: nums = [-1,-2,3,4], k = 3
    Output: [-1,3,4]
    Explanation:
    The subsequence has the largest sum of -1 + 3 + 4 = 6.

    Example 3:
    Input: nums = [3,4,3,3], k = 2
    Output: [3,4]
    Explanation:
    The subsequence has the largest sum of 3 + 4 = 7.
    Another possible subsequence is [4, 3].

    Constraints:
    1 <= nums.length <= 1000
    -105 <= nums[i] <= 105
    1 <= k <= nums.length

    Kth Largest Element in an Array
    Maximize Sum Of Array After K Negations
    Sort Integers by The Number of 1 Bits
    Minimum Difference in Sums After Removal of Elements

    Array Hash Table Sorting Heap (Priority Queue)
    '''
    @staticmethod
    def maxSubsequence(nums, k):
        ans, mn = [], nums[0]
        for i, x in enumerate(nums):
            if i > k - 1:
                mn = min(ans)
                if x > mn:
                    del ans[ans.index(mn)]
                    ans.append(x)
            else:
                ans.append(x)
        return ans

    @staticmethod
    def maxSubsequence1(nums, k):
        mh, res = [], []
        for i, x in enumerate(nums):
            heappush(mh, (-x, i))
        for _ in range(k):
            res.append(heappop(mh))
        return [-x[0] for x in sorted(res, key=lambda x: x[1])]
print(Solution.maxSubsequence([2,1,3,3], 2))