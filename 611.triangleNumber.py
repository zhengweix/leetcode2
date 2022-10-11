class Solution:
    '''
    Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
    Example 1:
    Input: nums = [2,2,3,4]
    Output: 3
    Explanation: Valid combinations are:
    2,3,4 (using the first 2)
    2,3,4 (using the second 2)
    2,2,3

    Example 2:
    Input: nums = [4,2,3,4]
    Output: 4

    Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000

    Array, Two Pointers, Binary Search, Greedy, Sorting

    3Sum Smaller
    '''
    def triangleNumber(self, nums):
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            lo, hi = 0, i-1
            while lo < hi:
                if nums[hi] + nums[lo] > nums[i]:
                    ans += hi - lo
                    hi -= 1
                else:
                    lo += 1
        return ans

    def main(self):
        print(self.triangleNumber([2,2,3,4]))

S = Solution()
S.main()