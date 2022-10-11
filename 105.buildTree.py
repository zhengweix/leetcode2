# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

    Example 1:
    https://assets.leetcode.com/uploads/2021/02/19/tree.jpg
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

    Example 2:

    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

    Constraints:
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.

    Array, Hash TableD, ivide and Conquer, Tree, Binary Tree
    '''
    def buildTree(self, preorder, inorder):
        mp, stack, root = {x: i for i, x in enumerate(inorder)}, [], None
        for x in preorder:
            if not root:
                root = node = TreeNode(x)
            elif mp[x] < mp[node.val]:
                stack.append(node)
                node.left = node = TreeNode(x)
            else:
                while stack and mp[stack[-1].val] < mp[x]:
                    node = stack.pop()
                node.right = node = TreeNode(x)
        return root

    def buildTree1(self, preorder, inorder):
        if not preorder:
            return None
        root, mid = TreeNode(preorder[0]), inorder.index(preorder[0])
        root.left = self.buildTree1(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree1(preorder[mid+1:], inorder[mid+1:])
        return root
