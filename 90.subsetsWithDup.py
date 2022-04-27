class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        list.sort(nums)
        lists = [[]]
        for n in nums:
            nn = len(lists)
            for i in range(nn):
                set = list(lists[i])
                set.append(n)
                if set not in lists:
                    lists.append(set)

        return lists
