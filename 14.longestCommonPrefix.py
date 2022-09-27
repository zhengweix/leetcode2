class Solution:
    '''
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

    Compare Version Numbers, Design In-Memory File System, Next Palindrome Using Same Digits
    '''
    def longestCommonPrefix(self, strs):
        n = 0
        prefix = ''
        m = len(min(strs))
        while n < m:
            for str in strs:
                if strs[0][n] != str[n]:
                    return prefix
            prefix += strs[0][n]
            n += 1
        return prefix

    def longestCommonPrefix1(self, strs):
        if not strs:
            return ''
        for i, c in enumerate(zip(*strs)):
            if len(set(c)) > 1:
                return strs[0][:i]
        return min(strs)

    def main(self):
        x = ["dog","racecar","car"]
        print(tuple(min(x)))

S = Solution()
S.main()