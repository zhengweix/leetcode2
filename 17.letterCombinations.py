from itertools import *
class Solution:
    '''
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    Example 1:
    https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Example 2:
    Input: digits = ""
    Output: []

    Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

    Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

    Hash Table, String, Backtracking

    22. Generate Parentheses
    39. Combination Sum
    2266. Count Number of Texts
    '''
    @staticmethod
    def letterCombinations(digits):
        mp = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def helper(digits, combo):
            if not digits:
                ans.append(combo)
            else:
                for c in mp[int(digits)-2]:
                    helper(digits[1:], combo+c)
        ans = []
        helper(digits, '')
        return ans

    @staticmethod
    def letterCombinations1(digits):
        mp = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits:
            return []
        chs = [mp[int(d)-2] for d in digits]
        ans = ['']
        for c in chs:
            ans = [x+y for x in ans for y in c]
        return ans

print(Solution.letterCombinations1('23'))
