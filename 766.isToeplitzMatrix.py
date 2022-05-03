class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for x in range(1, len(matrix)):
            for y in range(1, len(matrix[0])):
                if matrix[x][y] != matrix[x-1][y-1]:
                    return False
        return True
        #return all(r1[:-1] == r2[1:] for r1, r2 in zip(matrix, matrix[1:]))