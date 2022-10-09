class Solution:
    '''
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

    Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

    Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

    Next challenges:
    130 286 305 323 694 695 1905 1992
    '''
    def numIslands(self, grid):
        if not grid:
            return 0
        def helper(x, y):
            ''' Flood filling with '0'. '''
            grid[y][x] = '0'
            for x1, y1 in (x-1, y), (x, y-1), (x, y+1), (x+1, y):
                if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid) and grid[y1][x1] != '0':
                    helper(x1, y1)
        ans = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != '0':
                    ans += 1
                    helper(x, y)
        return ans