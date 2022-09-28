class Solution:
    '''
    Write an algorithm to determine if a number n is happy.
    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.

    Example 1:
    Input: n = 19
    Output: true
    Explanation:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 82 = 100
    1^2 + 0^2 + 0^2 = 1

    Example 2:
    Input: n = 2
    Output: false

    Constraints:
    1 <= n <= 231 - 1

    Hash Table, Math, Two Pointers

    Linked List Cycle, Add Digits, Ugly Number, Sum of Digits of String After Convert
    '''

    #* unhappy numbers eventually get stuck in cycle 4->16->37->58->89->145->42->20.
    # tc: O(logn) sc: O(1)
    def isHappy1(self, n):
        while n != 1 and n != 4:
            n = lambda n: sum(int(x)**2 for x in str(n))
        return n == 1

    # tc: O(logn) sc: O(1)
    def isHappy(self, n):
        helper = lambda n: sum(int(x)**2 for x in str(n))
        slow, fast = n, helper(n)
        while fast != slow:
            slow = helper(slow)
            fast = helper(helper(fast))
        return slow == 1

    def main(self):
        print(self.isHappy(2))

S = Solution()
S.main()





