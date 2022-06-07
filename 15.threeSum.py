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
    16 18 259
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len1, res = len(nums), []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left, right = i + 1, len1 - 1
            while left < right:
                sum1 = num + nums[left] + nums[right]
                if sum1 > 0:
                    right -= 1
                elif sum1 < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res