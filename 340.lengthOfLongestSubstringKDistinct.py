from collections import defaultdict
class Solution:
    '''
    Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

    Example 1:
    Input: s = "eceba", k = 2
    Output: 3
    Explanation: The substring is "ece" with length 3.

    Example 2:
    Input: s = "aa", k = 1
    Output: 2
    Explanation: The substring is "aa" with length 2.

    Constraints:
    1 <= s.length <= 5 * 104
    0 <= k <= 50

    Hash Table, String, Sliding Window
    '''
    @staticmethod
    def lengthOfLongestSubstringKDistinct(s, k):
        ans, start, mp = 0, 0, {}
        for end, c in enumerate(s):
            mp[c] = 1 + mp.get(c, 0)
            while len(mp) > k:
                for x in s[start:end]:
                    mp[x] -= 1
                    if mp[x] == 0:
                        del mp[x]
                    start += 1
            ans = max(end - start + 1, ans)
        return ans
print(Solution.lengthOfLongestSubstringKDistinct("eceba", 2))











