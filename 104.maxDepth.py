# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, maxDepth):
            if not node:
                return maxDepth
            maxDepth += 1
            return max(helper(root.left, maxDepth), helper(root.right, maxDepth))

        return helper(root, 0)