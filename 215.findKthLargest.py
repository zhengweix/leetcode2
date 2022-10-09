from heapq import *
from random import *
class Solution:
    '''
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

    Constraints:
    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104

    Array， Divide and Conquer， Sorting, Heap (Priority Queue), Quickselect
    Wiggle Sort II, Top K Frequent Elements, Third Maximum Number, Kth Largest Element in a Stream, K Closest Points to Origin, Find the Kth Largest Integer in the Array, Find Subsequence of Length K With the Largest Sum, K Highest Ranked Items Within a Price Range
    #324 973 1985 2146 414 703 2099
    '''
    # tc: O(nlogn)
    def findKthLargest(self, nums, k):
        pg = []
        for num in nums:
            heappush(pq, -num)
        i, ans = 0, None
        while i < k:
            ans = -heappop(pg)
            i += 1
        return ans

    # tc: O(nlogn)
    def findKthLargest1(self, nums, k):
        pg = []
        for x in nums:
            heappush(pq, x)
            if len(pg) > k:
                heappop(pq)
        return pq[0]
        # return nlargest(k, nums)[-1]

    # tc: O(nlogn)
    def findKthLargest2(self, nums, k):
        return sorted(nums)[-k]

    #* tc O(n)
    def findKthLargest3(self, nums, k):
        '''Quickselect'''
        def helper(lo, hi):
            p = randint(lo, hi) # random pivot
            nums[hi], nums[p] = nums[p], nums[hi]
            i = lo
            while i < hi:
                if nums[i] < nums[hi]:
                    nums[lo], nums[i] = nums[i], nums[lo]
                    lo += 1
                i += 1
            nums[lo], nums[hi] = nums[hi], nums[lo]
            return lo

        lo, hi = 0, len(nums)-1
        while lo < hi:
            p = helper(lo, hi)
            if p + k > len(nums):
                hi = p
            elif p + k < len(nums):
                lo = p + 1
            else:
                return nums[p]

    def main(self):
        print(self.findKthLargest3([3,2,3,1,2,4,5,5,6], 4))

S = Solution()
S.main()