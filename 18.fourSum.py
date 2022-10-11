class Solution:
    '''
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.

    Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]

    Constraints:
    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109

    Array, Two Pointers, Sorting

    Two Sum, 3Sum, 4Sum II, Count Special Quadruplets
    '''
    def fourSum(self, nums, target):
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                #! do not forget j > i+1
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j+1, len(nums)-1
                while lo < hi:
                    sm = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if sm == target:
                        ans.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                    elif sm > target:
                        hi -= 1
                    else:
                        lo += 1
        return ans

    def main(self):
        print(self.fourSum([2,2,2,2,2], 8))

S = Solution()
S.main()