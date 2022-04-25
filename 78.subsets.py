class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lists = [[]]
        for n in nums:
            i = 0
            nn = len(lists)
            for i in range(nn):
                set = list(lists[i])
                set.append(n)
                lists.append(set)

        return lists