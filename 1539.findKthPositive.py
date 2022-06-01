class Solution:
    '''
    Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
    Return the kth positive integer that is missing from this array.

    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

    Input: arr = [1,2,3,4], k = 2
    Output: 6
    Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

    Constraints:
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length
    '''
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 1, 0
        while j < k:
            if i not in arr:
                num = i
                j += 1
            i += 1
        return num

    def findKthPositive1(self, arr: List[int], k: int) -> int:
        num, miss, i = 1, 0, 0
        n = len(arr)
        while i < n:
            if arr[i] != num:
                miss += 1
                if miss == k:
                    return num
            else:
                i += 1
            num += 1
        return arr[n-1] + k - miss
#2195