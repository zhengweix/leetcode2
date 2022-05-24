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
    '''
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if root.val == targetSum and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, currentSum):
            if node:
                currentSum += node.val
                if currentSum == targetSum and not node.left and not node.right:
                    return True
                else:
                    return helper(node.left, currentSum) or helper(node.right, currentSum)

        return True if helper(root, 0) else False
#113 437 666 129