class Solution:
    '''
    Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

    Example 1:
    Input: nums = [-2,0,1,3], target = 2
    Output: 2
    Explanation: Because there are two triplets which sums are less than 2:
    [-2,0,1]
    [-2,0,3]

    Example 2:
    Input: nums = [], target = 0
    Output: 0

    Example 3:
    Input: nums = [0], target = 0
    Output: 0

    Constraints:
    n == nums.length
    0 <= n <= 3500
    -100 <= nums[i] <= 100
    -100 <= target <= 100

    Array, Two Pointers, Binary Search, Sorting

    3Sum, 3Sum Closest, Valid Triangle Number, Two Sum Less Than K
    '''
    # tc: O(n^2) sc: O(n)
    # input: [-2,0,1,3], 4
    def threeSumSmaller(self, nums, target):
        ans = 0
        nums.sort() #[-2,0,1,3]
        if len(nums) >= 3:
            for i in range(len(nums)-2):
                lo, hi = i+1, len(nums) - 1
                while lo < hi:
                    sm = nums[i] + nums[lo] + nums[hi]
                    if sm < target:
                        ans += hi - lo
                        lo += 1
                    else:
                        hi -= 1
        return ans

    def main(self):
        print(self.threeSumSmaller([-2,0,1,3], 4))

S = Solution()
S.main()
