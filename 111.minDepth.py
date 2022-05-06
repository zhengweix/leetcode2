# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, minDepth):
            if not node:
                return minDepth
            minDepth += 1
            if node.left and node.right:
                return min(helper(node.left, minDepth), helper(node.right, minDepth))
            elif node.left:
                return helper(node.left, minDepth)
            else:
                return helper(node.right, minDepth)

        return helper(root, 0)
#510 666 426