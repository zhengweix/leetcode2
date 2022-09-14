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
    #? keywords: average, greater than or equal, subset of k
    #? the number of sub-arrays
    #? approach: sliding window
    # input: arr - [2,2,2,2,5,5,5,8]
    #        k = 3
    #        threshold = 4
    # output: 3
    def numOfSubarrays1(self, arr, k, threshold):
        ans, winStart, winSum = 0, 0, 0
        for winEnd, v in enumerate(arr): # winEnd = k - 1
            winSum += v # [2,2,2],[2,2,2],[2,2,5],[2,5,5],[5,5,5],[5,5,8]
            if winEnd >= k-1:
                if winSum / k >= threshold: # 2,2,3,4,5,6
                    ans += 1 # 0,0,0,1,2,3
                winSum -= arr[winStart] # 4,4,7,10,10,13
                winStart += 1 #1,2,3,4,5,6
        return ans

    def numOfSubarrays1(self, arr, k, threshold):
        ans, winSum = 0, 0
        for winEnd, v in enumerate(arr):
            winSum += v
            if winEnd >= k:
                winSum -= arr[winEnd-k]
            if winEnd >= k-1 and winSum >= threshold*k:
                ans += 1
        return ans

    def main(self):
        print(self.numOfSubarrays1([2,2,2,2,5,5,5,8], 3, 4))

S = Solution()
S.main()