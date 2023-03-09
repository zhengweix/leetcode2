class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

    Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

    Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

    Related Topics
    Array, Binary Search, Divide and Conquer

    More challenges
    2387. Median of a Row Wise Sorted Matrix
    """
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        #* avoid list index out of range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            mid = (lo + hi)//2
            mid1 = (m + n)//2 - mid
            if mid > 0 and nums1[mid-1] > nums2[mid1]:
                hi = mid
            elif mid < m and nums1[mid] < nums2[mid1-1]:
                lo = mid+1
            else:
                if mid == m:
                    r = nums2[mid1]
                elif mid1 == n:
                    r = nums1[mid]
                else:
                    r = min(nums1[mid], nums2[mid1])

                if (m+n)%2:
                    return r
                if mid == 0:
                    l = nums2[mid1-1]
                elif mid1 == 0:
                    l = nums1[mid-1]
                else:
                    l = max(nums1[mid-1], nums2[mid1-1])
                return (l + r)/2

print(Solution.findMedianSortedArrays([3, 8, 9, 10], [2, 4, 6, 12, 18, 20]))