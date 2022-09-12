class Solution:
    '''
    Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

    Example 1:
    Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
    Output: 3
    Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

    Example 2:
    Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
    Output: 6
    Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

    Constraints:
    1 <= arr.length <= 105
    1 <= arr[i] <= 104
    1 <= k <= arr.length
    0 <= threshold <= 104

    Related Topics
    Array, Sliding Window

    Next Challeges:
    K Radius Subarray Averages
    '''
    def numOfSubarrays(self, arr, k, threshold):
        res = 0
        winSum, winStart = 0, 0
        for winEnd in range(len(arr)):
            winSum += arr[winEnd]
            if winEnd >= k-1:
                if winSum/k >= threshold:
                    res += 1
                winSum -= arr[winStart]
                winStart += 1
        return res

    def main(self):
        print(self.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))

S = Solution()
S.main()