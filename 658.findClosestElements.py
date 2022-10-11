class Solution:
    '''
    Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
    An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

    Example 1:
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

    Example 2:
    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]

    Constraints:
    1 <= k <= arr.length
    1 <= arr.length <= 104
    arr is sorted in ascending order.
    -104 <= arr[i], x <= 104

    Array, Two Pointers, Binary Search, Sorting, Heap (Priority Queue)

    Guess Number Higher or Lower, Guess Number Higher or Lower II, Find K-th Smallest Pair Distance, Find Closest Number to Zero
    '''
    # tc: O(n) sc: O(k)
    def findClosestElements(self, arr, k, x):
        def helper(xx):
            lo, hi = 0, len(arr)-1
            while lo < hi:
                mid = lo + hi >> 1
                if arr[mid] == xx:
                    return mid
                if arr[mid] > xx:
                    if (mid > 0 and arr[mid - 1] < xx):
                        return helper2(mid-1, mid, xx)
                    hi = mid
                else:
                    if (mid < len(arr)-1 and arr[mid + 1] > xx):
                        return helper2(mid, mid+1, xx)

                    lo = mid + 1
            return lo

        def helper2(val1, val2, xxx):
            if (xxx - arr[val1] > arr[val2] - xxx):
                return val2
            else:
                return val1

        s = helper(x)
        ans = [arr[s]]
        k -= 1
        left = s - 1 if s > 0 else -1
        right = s + 1 if s < len(arr) - 1 else len(arr)
        while left >= 0 and right <= len(arr) - 1:
            if k == 0:
                return sorted(ans)
            if x - arr[left] <= arr[right] - x:
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
            k -= 1

        while left >= 0:
            if k == 0:
                return sorted(ans)
            ans.append(arr[left])
            left -= 1
            k -= 1

        while right <= len(arr) - 1:
            if k == 0:
                return sorted(ans)
            ans.append(arr[right])
            right += 1
            k -= 1

        return sorted(ans)

    def findClosestElements1(self, arr, k, x):
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = lo + hi >> 1
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]

    def main(self):
        print(self.findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))

S = Solution()
S.main()