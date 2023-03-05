from random import shuffle
class Solution:
    '''
    Given an array of integers nums, sort the array in ascending order and return it.
    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

    Example 1:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]
    Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

    Example 2:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
    Explanation: Note that the values of nums are not necessairly unique.

    Constraints:
    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
    '''
    #! Time Limit Exceeded
    @staticmethod
    def sortArray(nums):
        def helper(lo, hi): # Partition
            i, p = lo, nums[hi]
            for j in range(lo, hi):
                if nums[j] <= p:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[hi] = nums[hi], nums[i]
            return i

        def helper1(lo, hi): # QuickSort
            if lo >= hi:
                return
            mid = helper(lo, hi)
            helper1(lo, mid-1)
            helper1(mid+1, hi)

        helper1(0, len(nums)-1)
        return nums

    @staticmethod
    def sortArray1(nums):
        shuffle(nums)
        def helper(lo, hi):
            i, j = lo + 1, hi - 1
            while i <= j:
                if nums[i] < nums[lo]:
                    i += 1
                elif nums[j] > nums[lo]:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[lo], nums[j] = nums[j], nums[lo]
            return j

        def helper1(lo, hi):
            if lo + 1 >= hi:
                return
            mid = helper(lo, hi)
            helper1(lo, mid)
            helper1(mid+1, hi)

        helper1(0, len(nums))
        return nums

print(Solution.sortArray1([5,1,1,2,0,0]))