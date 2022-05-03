class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        lr, lc = len(grid), len(grid[0])
        for r in range(lr):
            for c in range(lc):
                if grid[r][c] == 1:
                    if perimeter != 0:
                        if r > 0 and grid[r-1][c] == 1:
                            perimeter -= 2
                        if c > 0 and grid[r][c-1] == 1:
                            perimeter -= 2
                    perimeter += 4
        return perimeter
#695 1034