import sys


class PathNode:
    def __init__(self, val):
        self.val = val
        self.child = []

    def addChild(self, node):
        self.child.append(node)

class Solution:
    '''
    The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.
    Take for example the tree below:
    https://raw.githubusercontent.com/ramsayleung/leetcode/master/images/2020-04-27_21-32-39_img_01.png

    A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).
    Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.
    Implement your function in the most efficient manner and analyze its time and space complexities.
    For example:
    Given the rootNode of the tree in diagram above
    Your function would return:
    7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

    Constraints:
    [time limit] 5000ms
    [input] Node rootNode
    0 ≤ rootNode.cost ≤ 100000
    [output] integer
    '''
    def salesPath(self, root):
        print(root.val)
        if len(root.child) == 0:
            return root.val

        res = sys.maxsize
        for node in root.child:
            cost = self.salesPath(node)
            if cost < res:
                res = cost
        return res + root.val

    def main(self):
        node = PathNode(4)
        node0 = PathNode(5)
        node0.addChild(node)
        node1 = PathNode(1)
        node2 = PathNode(1)
        node2.addChild(node1)
        node3 = PathNode(2)
        node3.addChild(node2)
        node4 = PathNode(10)
        node5 = PathNode(0)
        node5.addChild(node4)
        node6 = PathNode(3)
        node6.addChild(node5)
        node6.addChild(node3)
        node7 = PathNode(1)
        node8 = PathNode(5)
        node9 = PathNode(6)
        node9.addChild(node7)
        node9.addChild(node8)

        root = PathNode(0)
        root.addChild(node0)
        root.addChild(node6)
        root.addChild(node9)
        print(self.salesPath(root))
S = Solution()
S.main()