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
    Longest Substring with At Most Two Distinct Characters
    Longest Substring with At Most K Distinct Characters
    Subarrays with K Different Integers
    Maximum Erasure Value
    Number of Equal Count Substrings
    Minimum Consecutive Cards to Pick Up
    Longest Nice Subarray
    Optimal Partition of String

    Hash Table, String, Sliding Window
    '''
    def lengthOfLongestSubstring(self, s):
        '''Using a dictionary ch to keep track of visited chars and their last positions in string. While moving a pointer i forward, if s[end] has seen before, move anchor start (forward only) to 1 + ch[c] to make sure no duplicates between start and end.'''
        ans, start, ch = 0, 0, {}
        for end, c in enumerate(s):
            if c in ch:
                start = max(start, ch[c]+1)
            ans = end - start + 1
            ch[c] = end
        return ans

    def main(self):
        print(self.lengthOfLongestSubstring("pwwkew"))

S = Solution()
S.main()






























