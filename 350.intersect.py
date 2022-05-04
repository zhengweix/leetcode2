class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intsec = []
        l1, l2 = len(nums1), len(nums2)
        nums = nums1 if l1 <= l2 else nums2
        nums_ = nums2 if l1 <= l2 else nums1
        for n in nums:
            if n in nums_:
                intsec.append(n)
                del nums_[nums_.index(n)]

        return intsec
#2143