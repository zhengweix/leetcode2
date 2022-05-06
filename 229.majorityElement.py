class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dct, lst = defaultdict(int), []
        for n in nums:
            dct[n] += 1
            if dct[n] > len(nums)/3 and n not in lst:
                lst.append(n)

        return lst