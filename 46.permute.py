class Solution:
    '''
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Example 3:
    Input: nums = [1]
    Output: [[1]]

    Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

    Array, Backtracking

    47. Permutations II
    60. Permutation Sequence
    77. Combinations
    '''
    @staticmethod
    def permute(nums):
        ans = [[]]
        for x in nums:
            temp = []
            for ele in ans:
                ele.append(x)
                for i in range(len(ele)):
                    ele[i], ele[-1] = ele[-1], ele[i]
                    temp.append(ele[:])
                    ele[i], ele[-1] = ele[-1], ele[i]
            ans = temp
        return ans

    @staticmethod
    def permute1(nums):
        def helper(ele, temp):
            if len(ele) == 1:
                ans.append(temp + ele)
                return
            for i in range(len(ele)):
                helper(ele[:i]+ele[i+1:], temp+[ele[i]])

        ans = []
        helper(nums, [])
        return ans

print(Solution.permute1([1,2,3]))
