# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
    A leaf is a node with no children.

    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Explanation: The root-to-leaf path with the target sum is shown.

    Input: root = [1,2,3], targetSum = 5
    Output: false
    Explanation: There two root-to-leaf paths in the tree:
    (1 --> 2): The sum is 3.
    (1 --> 3): The sum is 4.
    There is no root-to-leaf path with sum = 5.

    Input: root = [], targetSum = 0
    Output: false
    Explanation: Since the tree is empty, there are no root-to-leaf paths.

    Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

    Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Next challenges:
    113 437 666 129
    Path Sum II, Binary Tree Maximum Path Sum, Sum Root to Leaf Numbers, Path Sum III, Path Sum IV
    '''
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum1(self, root, targetSum):
        if not root:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum2(self, root, targetSum):
        stack = [(root, 0)]
        while stack:
            node, sm = stack.pop()
            if node:
                sm += node.val
                if not node.left and not node.right and sm == targetSum:
                    return True
                if node.right:
                    stack.append((node.right, sm))
                if node.left:
                    stack.append((node.left, sm))
        return False