'''
Write a function that takes in a sorted array of distinct integers
and returns the first index in the array that is equal to the value at that index.
In other words, your function should return the minimum index where
index == array[index]
input:   "array": [-5, -3, 0, 3, 5, 6, 10]
output: 3
'''
def findValue(arr):
    lo, hi = 0, len(arr)
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == arr[mid]:
            ans = mid
            hi = mid - 1
        elif mid < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return cache

print(findValue([-5, -3, 0, 3, 5, 6, 10]))