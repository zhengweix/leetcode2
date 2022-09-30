class Solution:
    '''
    Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
    If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
    Note that the word should be built from left to right with each additional character being added to the end of a previous word.

    Example 1:
    Input: words = ["w","wo","wor","worl","world"]
    Output: "world"
    Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

    Example 2:
    Input: words = ["a","banana","app","appl","ap","apply","apple"]
    Output: "apple"
    Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

    Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 30
    words[i] consists of lowercase English letters.

    Array, Hash Table, String, Trie, Sorting

    Longest Word in Dictionary through Deleting, Implement Magic Dictionary, Longest Word With All Prefixes
    '''
    def longestWord(self, words):
        def helper(word):
            n = len(word) - 1
            while n > 0:
                if word[:n] not in words:
                    return False
                n -= 1
            return True

        for word in sorted(words, key=lambda x: (-len(x), x)):
            if helper(word):
                return word
        return ''

    def main(self):
        print(self.longestWord(["w","wo","wor","worl","world"]))

S = Solution()
S.main()