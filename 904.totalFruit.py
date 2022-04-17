class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        dict = {}
        d = 0
        for end, fruit in enumerate(fruits):
            if fruit not in dict:
                dict[fruit] = 0
            dict[fruit] += 1
            while len(dict) > 2:
                fruit_ = fruits[start]
                dict[fruit_] -= 1
                if dict[fruit_] == 0:
                    del dict[fruit_]
                start += 1
            d = max(d, end - start + 1)
        return d