class Solution:
    '''
    Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
    The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

    Example 1:
    Input: nums = [1,2,1]
    Output: [2,-1,2]
    Explanation: The first 1's next greater number is 2;
    The number 2 can't find next greater number.
    The second 1's next greater number needs to search circularly, which is also 2.

    Example 2:
    Input: nums = [1,2,3,4,3]
    Output: [2,3,4,-1,4]

    Constraints:
    1 <= nums.length <= 104
    -109 <= nums[i] <= 109

    Array, Stack, Monotonic Stack

    Next Greater Element I, Next Greater Element III
    '''
    #! circularly search
    def nextGreaterElements(self, nums):
        ans, stack = [-1]*len(nums), []
        for i, x in enumerate(nums+nums):
            while stack and stack[-1][1] < x:
                ans[stack.pop()[0]] = x
            stack.append((i%len(nums), x))
        return ans

    def main(self):
        print(self.nextGreaterElements(
[100,1,11,1,120,111,123,1,-1,-100]))

S = Solution()
S.main()