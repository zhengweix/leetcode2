class Solution:
    '''
    Given an unsorted integer array nums, return the smallest missing positive integer.
    You must implement an algorithm that runs in O(n) time and uses constant extra space.

    Example 1:
    Input: nums = [1,2,0]
    Output: 3
    Explanation: The numbers in the range [1,2] are all in the array.

    Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2
    Explanation: 1 is in the array but 2 is missing.

    Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1
    Explanation: The smallest positive integer 1 is missing.

    Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1

    Array, Hash Table

    Missing Number,
    Find the Duplicate Number,
    Find All Numbers Disappeared in an Array,
    Couples Holding Hands,
    Smallest Number in Infinite Set
    '''
    # tc: O(n) sc: O(1)
    @staticmethod
    def firstMissingPositive(nums):
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i]> 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        for i, n in enumerate(nums):
            if i+1 != n:
                return i+1
        return n+1

    # tc: O(nlogn) sc: O(1)
    @staticmethod
    def firstMissingPositive1(nums):
        nums.sort()
        ans = 1
        for i in range(len(nums)):
            if nums[i] == ans:
                ans += 1
        return ans

    @staticmethod
    def firstMissingPositive2(nums):
        nums = set(nums)
        return min([i for i in range(1, len(nums) + 2) if i not in nums])

print(Solution.firstMissingPositive2([-5, -2, -10, 3, 4, 2]))