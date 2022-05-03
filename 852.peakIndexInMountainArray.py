class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = len(arr)
        start, end = 0, l-1
        while end > start:
            mid = int((start + end) / 2)
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                end = mid
            else:
                start = mid + 1