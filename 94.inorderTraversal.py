# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree, return the inorder traversal of its nodes' values.

    Example 1:
    https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg
    Input: root = [1,null,2,3]
    Output: [1,3,2]

    Example 2:
    Input: root = []
    Output: []

    Example 3:
    Input: root = [1]
    Output: [1]

    Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

    Stack, Tree, Depth-First Search, Binary Tree

    Binary Tree Preorder Traversal, Binary Tree Postorder Traversal, Binary Search Tree Iterator, Closest Binary Search Tree Value II, Inorder Successor in BST, Convert Binary Search Tree to Sorted Doubly Linked List, Minimum Distance Between BST Nodes
    '''
    def inorderTraversal(self, root):
        def helper(node):
            if not node:
                return
            helper(node.left)
            ans.append(node.val)
            helper(node.right)

        ans = []
        helper(root)
        return ans