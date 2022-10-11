class Solution:
    '''
    Given a pattern and a string s, find if s follows the same pattern.
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

    Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true

    Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false

    Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false

    Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.

    Hash Table, String

    Word Pattern II
    '''
    def wordPattern(self, pattern, s):
        ''' two mappings, define two mapping mp1 from pattern to index and mp2 from string to index. Then, we check if the mappings equal. If not, return False.'''
        s1 = s.split()
        if len(pattern) != len(s1): return False

        mp1, mp2 = {}, {}
        for i, (p, c) in enumerate(zip(pattern, s1)):
            if mp1.get(p) != mp2.get(c):
                return False
            mp1[p] = mp2[c] = i
        return True

    def wordPattern1(self, pattern, s):
        '''set length'''
        s1 = s.split()
        return len(set(pattern)) == len(set(s1)) == len(set(zip_longest(pattern, s1)))

    def wordPattern2(self, pattern, s):
        '''hash-ish'''
        f = lambda s: tuple(map({}.setdefault, s, range(len(s))))
        return f(pattern) == f(s.split())


    def main(self):
        print(self.wordPattern2("abba", "dog cat cat dog"))

S = Solution()
S.main()


