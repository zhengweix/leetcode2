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
    # [-3, 0, 1, 2, -1, 1, -2]
    # tc: O(n^2) sc: O(n)
    def threeSum(self, nums):
        def helper(nums1, target):
            lo, hi = 0, len(nums1)-1
            pairs = []
            while lo < hi:
                if nums1[lo] + nums1[hi] == target:
                    pairs.append([-target, nums1[lo], nums1[hi]])
                    hi -= 1
                    lo += 1
                    #* removing duplicates
                    while lo < hi and nums1[lo] == nums1[lo-1]:
                        lo += 1
                    while lo < hi and nums1[hi] == nums1[hi+1]:
                        hi -= 1
                elif nums1[lo] + nums1[hi] > target:
                    hi -= 1
                else:
                    lo += 1
            return pairs

        ans = []
        n = len(nums)
        if n > 2:
            nums.sort() # [-3, -2, -1, 0, 1, 1, 2]
            for i in range(n):
                #* removing duplicates
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                ans = ans + helper(nums[i+1:], -nums[i])
        return ans

    def main(self):
        print(self.threeSum([-3, 0, 1, 2, -1, 1, -2]))

S = Solution()
S.main()