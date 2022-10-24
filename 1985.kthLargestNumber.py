from heapq import *
class Solution:
    '''
    You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.
    Return the string that represents the kth largest integer in nums.
    Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

    Example 1:
    Input: nums = ["3","6","7","10"], k = 4
    Output: "3"
    Explanation:
    The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
    The 4th largest integer in nums is "3".

    Example 2:
    Input: nums = ["2","21","12","1"], k = 3
    Output: "2"
    Explanation:
    The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
    The 3rd largest integer in nums is "2".

    Example 3:
    Input: nums = ["0","0"], k = 2
    Output: "0"
    Explanation:
    The numbers in nums sorted in non-decreasing order are ["0","0"].
    The 2nd largest integer in nums is "0".

    Constraints:
    1 <= k <= nums.length <= 104
    1 <= nums[i].length <= 100
    nums[i] consists of only digits.
    nums[i] will not have any leading zeros.

    Best Meeting Point
    Special Array With X Elements Greater Than or Equal X
    Array With Elements Not Equal to Average of Neighbors
    '''
    def kthLargestNumber(self, nums, k):
        heap = []
        for x in nums:
            heappush(heap, -int(x))
        ans = -1
        while k > 0:
            ans = -heappop(heap)
            k -= 1

        return str(ans)

    def kthLargestNumber1(self, nums, k):
        return sorted(nums, key=int)[-k]

    def main(self):
        print(self.kthLargestNumber1(["3","6","7","10"], 4))

S = Solution()
S.main()