class Solution:
    '''
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.

    Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

    Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

    Constraints:
    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

    Follow up:
    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem in linear runtime complexity?

    Array, Two Pointers, Binary Search, Bit Manipulation

    Set Mismatch, First Missing Positive, Single Number, Linked List Cycle II, Missing Number, Set Mismatch
    '''
    def findDuplicate(self, nums):
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, n in enumerate(nums):
            if n != i + 1:
                return n

    def findDuplicate1(self, nums):
        #* mark the element if its index corresponding to the number has been seen. encounter the marked index again,
        for x in nums:
            nums[abs(x)-1] *= -1
            if nums[abs(x)-1] > 0: return abs(x)
    def main(self):
        print(self.findDuplicate([7,9,7,4,2,8,7,7,1,5]))

S = Solution()
S.main()