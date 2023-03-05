class Solution:
    '''
    Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

    Example 1:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

    Example 2:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

    Example 3:
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.

    Constraints:
    1 <= k <= num.length <= 105
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.

    String, Stack, Greedy, Monotonic Stack

    321. Create Maximum Number
    738. Monotone Increasing Digits
    1673. Find the Most Competitive Subsequence
    '''
    @staticmethod
    def removeKdigits(num, k):
        stack = []
        for x in num:
            while k and stack and stack[-1] > x:
                k -= 1
                stack.pop()
            stack.append(x)
        return ''.join(stack[:-k or None]).lstrip('0') or '0'  # <=> ans = stack[:-k] if k else stack
                                                               #     ans = ''.join(ans).lstrip('0')
                                                               #     return ans if ans else '0'

print(Solution.removeKdigits('9', 1))