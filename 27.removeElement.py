class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        if val in nums:
            idx = nums.index(val)
            while idx != None:
                del nums[idx]
                k -= 1
                if val not in nums:
                    return k
                else:
                    idx = nums.index(val)
        return k