# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree, invert the tree, and return its root.

    https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg
    Input: root = [2,1,3]
    Output: [2,3,1]

    Input: root = []
    Output: []

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

    Next challenges:
    536 743 431
    '''
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root