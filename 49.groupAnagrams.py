class Solution:
    '''
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Input: strs = [""]
    Output: [[""]]

    Input: strs = ["a"]
    Output: [["a"]]

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
