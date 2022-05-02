class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def helper(fill):
            if grid[0][0] == grid[1][1] == grid[2][2] == fill or grid[0][2] == grid[1][1] == grid[2][0] == fill or \
                    grid[0][0] == grid[0][1] == grid[0][2] == fill or grid[1][0] == grid[1][1] == grid[1][2] == fill or \
                    grid[2][0] == grid[2][1] == grid[2][2] == fill or grid[0][0] == grid[1][0] == grid[2][0] == fill or \
                    grid[0][1] == grid[1][1] == grid[2][1] == fill or grid[0][2] == grid[1][2] == grid[2][2] == fill:
                return True
            return False

        l = len(moves)
        grid = [[None for x in range(3)] for y in range(3)]
        for i, m in enumerate(moves):
            fill = 'O' if i % 2 else 'X'
            grid[m[0]][m[1]] = fill
            if helper('X'):
                return 'A'
            elif helper('O'):
                return 'B'
        if l < 9:
            return 'Pending'
        else:
            return 'Draw'
