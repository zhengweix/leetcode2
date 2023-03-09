class Solution:
    """
    Convert a non-negative integer num to its English words representation.

    Example 1:
    Input: num = 123
    Output: "One Hundred Twenty Three"

    Example 2:
    Input: num = 12345
    Output: "Twelve Thousand Three Hundred Forty Five"
    Example 3:

    Input: num = 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

    Constraints:
    0 <= num <= 231 - 1

    Related Topics
    Math, String, Recursion

    More challenges
    1418. Display Table of Food Orders in a Restaurant
    894. All Possible Full Binary Trees
    1016. Binary String With Substrings Representing 1 To N
    """
    @staticmethod
    def numberToWords(num):
        mp = {1: "One", 11: "Eleven", 10: "Ten",
              2: "Two", 12: "Twelve", 20: "Twenty",
              3: "Three", 13: "Thirteen", 30: "Thirty",
              4: "Four", 14: "Fourteen", 40: "Forty",
              5: "Five", 15: "Fifteen", 50: "Fifty",
              6: "Six", 16: "Sixteen", 60: "Sixty",
              7: "Seven", 17: "Seventeen", 70: "Seventy",
              8: "Eight", 18: "Eighteen", 80: "Eighty",
              9: "Nine", 19: "Nineteen", 90: "Ninety"}
        def helper(n):
            """Return English words of n (0-999) in array."""
            if not n:
                return []
            elif n < 20:
                return [mp[n]]
            elif n < 100:
                return [mp[n//10*10]] + helper(n%10)
            else:
                return [mp[n//100], "Hundred"] + helper(n%100)
        ans = []
        for i, unit in zip((9, 6, 3, 0), ("Billion", "Million", "Thousand", "")):
            n, num = divmod(num, 10**i)
            ans.extend(helper(n))
            if n and unit:
                ans.append(unit)
        return " ".join(ans) or "Zero"

print(Solution.numberToWords(2147483648))