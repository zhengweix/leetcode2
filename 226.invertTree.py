# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node:
                node.right, node.left = node.left, node.right
                helper(node.left)
                helper(node.right)

        helper(root)
        return root
#536 743 431