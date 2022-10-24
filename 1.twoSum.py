class Solution(object):
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]

    Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

    Next challenges:
    15 18 167 170 653 1099 1679 1711 2006 2023 2200
    Two Sum II - Input Array Is Sorted
    Two Sum III - Data structure design
    Two Sum IV - Input is a BST
    Two Sum Less Than K
    Max Number of K-Sum Pairs
    Count Good Meals
    Count Number of Pairs With Absolute Difference K
    Number of Pairs of Strings With Concatenation Equal to Target
    Find All K-Distant Indices in an Array
    First Letter to Appear Twice
    Number of Excellent Pairs
    Number of Arithmetic Triplets
    Node With Highest Edge Score
    Check Distances Between Same Letters
    Find Subarrays With Equal Sum
    Largest Positive Integer That Exists With Its Negative
    '''
    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            if v in d:
                return d[v], i
            d[target - v] = i