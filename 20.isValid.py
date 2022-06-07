class Solution:
    '''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Input: s = "()"
    Output: true

    Input: s = "()[]{}"
    Output: true

    Input: s = "(]"
    Output: false

    Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

    Next challenges:
    22 32 301 1003 2116
    '''
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        dict = {'}': '{', ']': '[', ')': '('}
        bkts = ['{', '[', '(']
        stack = []
        for c in s:
            if c in bkts:
                stack.append(c)
            elif stack and c == dict[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

    def isValid1(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            else:
                if len(stack) == 0:
                    return False
                if c != stack.pop():
                    return False
        return stack == []

