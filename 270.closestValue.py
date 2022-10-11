# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

    Example 1:
    https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg
    Input: root = [4,2,5,1,3], target = 3.714286
    Output: 4

    Example 2:
    Input: root = [1], target = 4.428571
    Output: 1

    Constraints:
    The number of nodes in the tree is in the range [1, 104].
    0 <= Node.val <= 109
    -109 <= target <= 109

    Tree, Depth-First Search, Binary Search Tree, Binary Search, Binary Tree

    Count Complete Tree Nodes, Closest Binary Search Tree Value II, Search in a Binary Search Tree
    '''
    def closestValue(self, root, target):
        def helper(node):
            if not node:
                return
            nonlocal ans
            if abs(node.val - target) < abs(ans - target):
                ans = node.val
            helper(node.left)
            helper(node.right)

        ans = root.val
        helper(root)
        return ans