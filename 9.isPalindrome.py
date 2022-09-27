from math import *
class Solution:
    '''
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.

    Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Constraints:
    -231 <= x <= 231 - 1

    Follow up:
    Could you solve it without converting the integer to a string?

    Palindrome Linked List, Find Palindrome With Fixed Length, Strictly Palindromic Number
    '''
    def isPalindrome(self, x):
        def helper(i):
            return x // 10**(int(log10(x))-i) % 10
        if x != abs(x):
            return False
        if x == 0:
            return True
        #! x can't be 0 for log0 is indeterminate
        lo, hi = 0, int(log10(x))
        while lo < hi:
            if helper(lo) != helper(hi):
                return False
            lo += 1
            hi -= 1
        return True

    def main(self):
        print(self.isPalindrome(0))

S = Solution()
S.main()