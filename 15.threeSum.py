class Solution:
    '''
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = []
    Output: []

    Input: nums = [0]
    Output: []

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105

    Next challenges:
    Two Sum, 3Sum Closest, 4Sum, 3Sum Smaller, Number of Arithmetic Triplets
    '''
    # nums[i] + nums[j]  == -nums[k]
    # tc: O(n^2) sc: O(n)
    @staticmethod
    def threeSum(nums):
        def helper(nums1, target):
            res, lo, hi = [], 0, len(nums1)-1
            while lo < hi:
                if nums1[lo] + nums1[hi] == target:
                    res.append([-target, nums1[lo], nums1[hi]])
                    hi -= 1
                    lo += 1
                    while lo < hi and nums1[lo] == nums1[lo-1]:
                        lo += 1
                    while lo < hi and nums1[hi] == nums1[hi+1]:
                        hi -= 1
                elif nums1[lo] + nums1[hi] > target:
                    lo += 1
                else:
                    hi -= 1
            return res

        ans = []
        n = len(nums)
        if n > 2:
            nums.sort()
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                ans += helper(nums[i+1:], -nums[i])
        return ans

print(Solution.threeSum([-2,0,1,1,2]))