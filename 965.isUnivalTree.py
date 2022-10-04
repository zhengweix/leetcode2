# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    A binary tree is uni-valued if every node in the tree has the same value.
    Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

    Example 1:
    Input: root = [1,1,1,1,1,null,1]
    Output: true

    Example 2:
    Input: root = [2,2,2,5,2]
    Output: false

    Constraints:
    The number of nodes in the tree is in the range [1, 100].
    0 <= Node.val < 100
    '''
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.right:
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right) and root.val == root.left.val and root.val == root.right.val

        elif root.left:
            return self.isUnivalTree(root.left) and root.val == root.left.val

        elif root.right:
            return self.isUnivalTree(root.right) and root.val == root.right.val

        return True

