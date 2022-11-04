class Solution:
    '''
    Given three sorted arrays A, B  and C of not necessarily same sizes.
    Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
    i.e. minimize | max(a,b,c) - min(a,b,c) |.

    Example :
    Input:
    A : [ 1, 4, 5, 8, 10 ]
    B : [ 6, 9, 15 ]
    C : [ 2, 3, 6, 6 ]
    Output:
    1
    Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
    '''
    @staticmethod
    def solve(arrs):
        def helper(arr):
            return abs(max(arr) - min(arr))
        mp, mp1 = [len(arr)-1 for arr in arrs], [arr[-1] for arr in arrs]
        ans = helper(mp1)
        while min(mp) >= 0:
            ans = min(ans, helper(mp1))
            mx = max(mp1)
            for i, x in enumerate(mp1):
                if x == mx:
                    mp[i] -= 1
                    mp1[i] = arrs[i][mp[i]]
                    break
        return ans

print(Solution.solve([[ 1, 4, 7, 8, 10 ], [ 6, 7, 9, 12, 15 ], [ 2, 3, 7, 9 ]]))