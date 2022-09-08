class Solution:
    '''
    Go through input matrix and find path in as output matrix.
    n = length of outer list 1 ... 10,000
    m = max length of inner list
    Input: [[2,4,5], [45, 67], [2, 3]]
    Output: [2, 45, 2], [2, 67, 2], [4, 45, 2] ... ]

    Related Topics
    Array, Backtracking, Bit Manipulation
    '''
    def findPath(self, pathList, nodes):
        pathList1 = []
        if not pathList:
            for node in nodes:
                pathList1.append([node])
        else:
            for node in nodes:
                for path in pathList:
                    path = path[:]
                    path.append(node)
                    pathList1.append(path)
        return pathList1

    def main(self):
        nodesList = [[2, 4, 5], [45, 67], [2, 3]]
        pathList = []
        n = len(nodesList)
        for i in range(n-1):
            pathList = self.findPath(pathList, nodesList[i])

        print(self.findPath(pathList, [nodesList[n-1][0]]))

S = Solution()
S.main()