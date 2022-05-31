class Solution:
    '''
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.

    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    Input: nums = [0]
    Output: [[],[0]]

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            n = len(subsets)
            for i in range(n):
                set = list(subsets[i])
                set.append(num)
                subsets.append(set)

        return subsets
#320 784 2044