class Solution:
    '''
    Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.

    Example 1:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".

    Example 2:
    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

    Example 3:
    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".

    Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

    Follow up: Can you solve it in O(n) time and O(1) space?
    '''
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(str, idx):
            cnt = 0
            while idx >= 0:
                if str[idx] == '#':
                    cnt += 1
                elif cnt > 0:
                    cnt -= 1
                else:
                    break
                idx -= 1
            return idx

        idx1, idx2 = helper(s, len(s)-1), helper(t, len(t)-1)
        while idx1 >= 0 and idx2 >= 0:
            if s[idx1] != t[idx2]:
                return False
            idx1 = helper(s, idx1-1)
            idx2 = helper(t, idx2-1)

        return idx1 == idx2

    def main(self):
        print(self.backspaceCompare("a#c", "b"))

S = Solution()
S.main()
