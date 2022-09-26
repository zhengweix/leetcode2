class Solution:
    '''
    Given a string s, find the length of the longest substring without repeating characters.

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Input: s = " "
    Output: 1

    Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

    Next challenges:
    159 340 992 1695 2067 2260

    Hash Table, String, Sliding Window
    '''
    def lengthOfLongestSubstring(self, s):
        ans, winStart = 0, 0
        chars = {}
        for winEnd, char in enumerate(s):
            if char in chars:
                winStart = max(winStart, chars[char]+1)
            chars[char] = winEnd
            ans = max(winEnd - winStart + 1, ans)
        return ans

    def main(self):
        print(self.lengthOfLongestSubstring("pwwkew"))

S = Solution()
S.main()






























