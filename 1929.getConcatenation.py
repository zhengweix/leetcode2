class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0 for i in range(2 * l)]
        for i, n in enumerate(nums):
            ans[i] = n
            ans[i + l] = n

        return ans
