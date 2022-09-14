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
    #? Does each node in one path be picked from different list and only 1 node from the last list as destination?
    #? My approach: to compute combination of subsets that contains nodes from different lists.
    #? Breadth-first search
    # tc: O(mn) sp: O(mn)
    def findPath(self, nodeList):
        #? create nested function to compute combinations to add new nodes to the paths
        # input: paths [[2], [4], [5]]
        #        nodes [45, 67]
        # output: [2, 45, 2], [2, 67, 2], [4, 45, 2] ... ]
        # tc: O(mn) sp: O(mn)
        def helper(paths, nodes):
            res = []
            for path in paths:
                #? make a shallpw copy to void adding node affects the iterating path list
                for node in nodes:
                    path1 = path[:]
                    #! 'NoneType' object has no attribute 'append' if nested append
                    path1.append(node)
                    res.append(path1)
            #? updated path list of iterating current nodes list
            return res # [[2, 45], [2, 67], [4, 45], [4, 67], [5, 45], [5, 67]

        # input: [[2, 4, 5], [45, 67], [2, 3]]
        paths = []
        for node in nodeList[0]: # [2, 4, 5]
            paths.append([node])
        #? middle node lists
        nodeList1 = nodeList[1:-1] # [[45, 67]]
        while nodeList1:
            #? freshed path list
            paths = helper(paths, nodeList1.pop(0))

        #? add destination
        ans = []
        dest = nodeList[len(nodeList)-1][0] # 2
        for path in paths:
            path.append(dest)
            ans.append(path)
        return ans #[[2, 45, 2], [2, 67, 2], [4, 45, 2], [4, 67, 2], [5, 45, 2], [5, 67, 2]

    def main(self):
        print(self.findPath([[2, 4, 5], [45, 67], [2, 3]]))

S = Solution()
S.main()