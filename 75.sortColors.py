class Solution:
    '''
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    You must solve this problem without using the library's sort function.

    Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Example 2:

    Input: nums = [2,0,1]
    Output: [0,1,2]

    Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

    Sort List, Wiggle Sort, Wiggle Sort II
    '''
    # [2,0,2,1,1,0]
    #* "Dijkstra's three-way partition
    def sortColors(self, nums):
        lo, mid, hi = 0, 0, len(nums)-1
        #! do not forget equals
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 2:
                nums[hi], nums[mid] = nums[mid], nums[hi]
                #! only decrease hi
                hi -= 1
            else:
                mid += 1

    def main(self):

        nums =  [2,0,2,1,1,0]
        self.sortColors(nums)
        print(nums)

S = Solution()
S.main()