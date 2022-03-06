# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.right:
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right) and root.val == root.left.val and root.val == root.right.val

        elif root.left:
            return self.isUnivalTree(root.left) and root.val == root.left.val

        elif root.right:
            return self.isUnivalTree(root.right) and root.val == root.right.val

        return True

