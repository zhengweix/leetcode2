class Solution:
    def countPoints(self, rings: str) -> int:
        l, n = len(rings)//2, []
        colors = {'R', 'G', 'B'}
        rods = defaultdict(set)
        for i in range(l):
            j = int(rings[2*i+1])
            rods[j].add(rings[2*i])
            if rods[j] & colors == colors and j not in n:
                n.append(j)
        return len(n)