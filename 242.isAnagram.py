class Solution:
    '''
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Input: s = "anagram", t = "nagaram"
    Output: true

    Input: s = "rat", t = "car"
    Output: false

    Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

    Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in s:
            t = t.replace(c, '', 1)
        return True if len(t) == 0 else False

    def isAnagram1(self, s: str, t: str) -> bool:
        return Counter(t) == Counter(s)

    def isAnagram2(self, s: str, t: str) -> bool:
        chars = {}





