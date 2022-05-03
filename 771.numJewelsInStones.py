class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        jewels = [c for c in jewels]
        for s in stones:
            if s in jewels:
                num += 1
        return num
#2024, 1912