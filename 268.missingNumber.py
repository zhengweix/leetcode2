from functools import *
from operator import *
class Solution:
    '''
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

    Constraints:
    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.

    Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting

    Follow up:
    Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

    #287 1980 41 765
    Couples Holding Hands, Find Unique Binary String
    '''
    # tc: O(n) sc: O(n)
    def missingNumber(self, nums):
        #* enumerate from 1 equivalent to 0 since 0 ^ x = x
        return reduce(xor, (i^x for i, x in enumerate(nums, 1)))

    # tc: O(n) sc: O(1)
    def missingNumber1(self, nums):
        #* gauss's formula
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

    def main(self):
        print(self.missingNumber1([10,9,6,4,2,3,5,7,0,1]))

S = Solution()
S.main()