class Solution:
    '''
    You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:
    If nums[i] is positive, move nums[i] steps forward, and
    If nums[i] is negative, move nums[i] steps backward.
    Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.
    A cycle in the array consists of a sequence of indices seq of length k where:
    Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
    Every nums[seq[j]] is either all positive or all negative.
    k > 1
    Return true if there is a cycle in nums, or false otherwise.

    Example 1:
    https://assets.leetcode.com/uploads/2022/09/01/img1.jpg
    Input: nums = [2,-1,1,2,2]
    Output: true
    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).

    Example 2:
    https://assets.leetcode.com/uploads/2022/09/01/img2.jpg
    Input: nums = [-1,-2,-3,-4,-5,6]
    Output: false
    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    The only cycle is of size 1, so we return false.

    Example 3:
    https://assets.leetcode.com/uploads/2022/09/01/img3.jpg
    Input: nums = [1,-1,5,1,4]
    Output: true
    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has a node jumping forward and a node jumping backward, so it is not a cycle.
    We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are white (jumping in the same direction).

    Constraints:
    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 1000
    nums[i] != 0

    Array, Hash Table, Two Pointers

    Grumpy Bookstore Owner, Minimum Absolute Difference Queries, Array With Elements Not Equal to Average of Neighbors
    '''
    def circularArrayLoop(self, nums):
        #* find next index of current pointer
        def helper(x):
            k = nums[x] + x
            if k >= 0:
                k %= len(nums)
            else:
                while k < 0:
                    k += len(nums)
            return k

        #* check whether the directions are same
        def helper2(num1, num2):
            return num1 * num2 > 0

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            slow = i
            fast = helper(i)
            while helper2(nums[slow], nums[fast]) and helper2(nums[fast], nums[helper(fast)]):
                #* cycle detected
                if slow == fast:
                    #* make sure k > 1
                    if helper(slow) == fast:
                        break
                    return True
                slow = helper(slow)
                fast = helper(helper(fast))

            idx = i
            while helper2(nums[idx], nums[i]):
                nums[idx] = 0
                idx = helper(idx)
        return False

    def main(self):
        print(self.circularArrayLoop([-2,1,-1,-2,-2]))

S = Solution()
S.main()