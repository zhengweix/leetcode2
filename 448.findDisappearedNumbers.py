class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, n, miss = 0, len(nums), []
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                miss.append(i + 1)
        return miss
#442 2195 1980