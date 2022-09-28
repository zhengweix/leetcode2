class Solution:
    '''
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

    Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

    Constraints:
    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

    Two Pointers, String, String Matching

    Shortest Palindrome
    '''
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        ans = -1
        if needle in haystack:
            p1 = p2 = 0
            while p1 < len(haystack) and p2 < len(needle):
                if haystack[p1] == needle[p2]:
                    if ans < 0:
                        ans = p1
                    p2 += 1
                else:
                    p1 = ans if ans >= 0 else p1
                    p2 = 0
                    ans = -1
                p1 += 1
        return ans

    def main(self):
        print(self.strStr('sadbutsad', 'sad'))

S = Solution()
S.main()