from heapq import *
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
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heappush(maxHeap, -num)

        i = 0
        while i < k:
            result = -heappop(maxHeap)
            i += 1

        return result

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
#324 973 1985 2146 414 703 2099