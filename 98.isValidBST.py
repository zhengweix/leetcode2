# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

    https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg
    Input: root = [2,1,3]
    Output: true

    https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

    Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

    Next challenges:
    501 94
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, low, high):
            if node is None:
                return True
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        return helper(root, None, None)