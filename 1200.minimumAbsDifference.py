from math import *
class Solution:
    """
    Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
    Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr
    """
    @staticmethod
    def minimumAbsDifference(arr):
        ans = []
        arr.sort()
        diff = inf
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] <= diff:
                if arr[i] - arr[i-1] < diff:
                    diff = arr[i] - arr[i-1]
                    ans = []
                ans.append([arr[i-1], arr[i]])
        return ans

print(Solution.minimumAbsDifference([1,3,6,10,15]))