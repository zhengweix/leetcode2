from re import *
class Solution:
    '''
    Given an encoded string, return its decoded string.
    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
    You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
    The test cases are generated so that the length of the output will never exceed 105.

    Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

    Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].

    Encode String with Shortest Length, Number of Atoms, Brace Expansion
    '''
    def decodeString(self, s):
        while findall('(\d+)\[([a-z]*)\]', s):
            for x in findall('(\d+)\[([a-z]*)\]', s):
                s = s.replace(x[0]+'['+x[1]+']', x[1]*int(x[0]))
        return s

    def decodeString1(self, s):
        stack = []
        ans = cnt = ''
        for c in s:
            if c.isalpha():
                ans += c
            elif c.isdigit():
                cnt += c
            elif c == '[':
                stack.append(cnt)
                stack.append(ans)
                ans = cnt = ''
            else:  # c == "]"
                ans = stack.pop() + ans * int(stack.pop())
        return ans
    def main(self):
        print(self.decodeString1('2[b3[a]]'))

S = Solution()
S.main()