class Solution:
    '''
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.

    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output:[[1,1,6], [1,2,5], [1,7], [2,6]]

    Input: candidates = [2,5,2,1,2], target = 5
    Output: [[1,2,2], [5]]

    Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

    Next challenges:
    39
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        dp = [[[]]] + [[] for x in range(target)]
        for cand in candidates:
            if cand > target:
                break
            for i in range(target, cand-1, -1):
                for lst in dp[i-cand]:
                    if lst + [cand] not in dp[i]:
                        dp[i].append(lst + [cand])
        return dp[target]