class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        intset = set1 & set2
        return [list(set1 - intset), list(set2 - intset)]
#2248