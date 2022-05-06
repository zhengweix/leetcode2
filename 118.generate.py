class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]]
        for i in range(1, numRows):
            lstRow = []
            for j in range(i + 1):
                if j == 0:
                    lstRow.append(lst[i - 1][j])
                elif j == i:
                    lstRow.append(lst[i - 1][j - 1])
                else:
                    lstRow.append(lst[i - 1][j] + lst[i - 1][j - 1])
            lst.append(lstRow)
        return lst