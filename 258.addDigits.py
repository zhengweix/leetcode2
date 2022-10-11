class Solution:
    '''
    Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

    Example 1:
    Input: num = 38
    Output: 2
    Explanation: The process is
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2
    Since 2 has only one digit, return it.

    Example 2:
    Input: num = 0
    Output: 0

    Constraints:
    0 <= num <= 231 - 1

    Follow up:
    Could you do it without any loop/recursion in O(1) runtime?

    Math, Simulation, Number Theory

    Sum of Digits in the Minimum Number, Sum of Digits of String After Convert, Minimum Sum of Four Digit Number After Splitting Digits, Calculate Digit Sum of a String
    '''
    # tc: O(1)
    def addDigits(self, num):
        if num < 9:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

    def addDigits1(self, num):
        #* and operator in case of num = 0
        return num and 1 + (num - 1) % 9

    def main(self):
        print(self.addDigits1(11110))

S = Solution()
S.main()