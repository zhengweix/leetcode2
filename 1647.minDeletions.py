from collections import *
class Solution:
    '''
    A string s is called good if there are no two different characters in s that have the same frequency.
    Given a string s, return the minimum number of characters you need to delete to make s good.
    The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

    Example 1:
    Input: s = "aab"
    Output: 0
    Explanation: s is already good.

    Example 2:
    Input: s = "aaabbbcc"
    Output: 2
    Explanation: You can delete two 'b's resulting in the good string "aaabcc".
    Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

    Example 3:
    Input: s = "ceabaacb"
    Output: 2
    Explanation: You can delete both 'c's resulting in the good string "eabaab".
    Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

    Constraints:
    1 <= s.length <= 105
    s contains only lowercase English letters.

    String, Greedy, Sorting

    2216. Minimum Deletions to Make Array Beautiful
    2091. Removing Minimum and Maximum From Array
    2423. Remove Letter To Equalize Frequency
    '''
    # tc: O(n) Counter(s) costs O(n), worst case of for and while loop is 26^2, sc: O(1)
    @staticmethod
    def minDeletions(s):
        mp, ans = {}, 0
        for key, cnt in Counter(s).items():
            while cnt in mp and cnt > 0:
                cnt -= 1
                ans += 1
            mp[cnt] = key
        return ans
print(Solution.minDeletions('bbcebab'))