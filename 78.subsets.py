class Solution:
    '''
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.

    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    Input: nums = [0]
    Output: [[],[0]]

    Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.

    Next challenges:
    320 784 2044
    320. Generalized Abbreviation
    784. Letter Case Permutation
    1982. Find Array Given Subset Sums
    '''
    @staticmethod
    def subsets(nums):
        ans = [[]]
        for x in nums:
            for i in range(len(ans)):
                if ans[i]+[x] not in ans:
                    ans.append(ans[i]+[x])
        return ans

print(Solution.subsets([1, 2, 3]))