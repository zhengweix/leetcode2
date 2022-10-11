# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

    Example 1:
    https://assets.leetcode.com/uploads/2021/02/19/tree.jpgß
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]

    Example 2:
    Input: inorder = [-1], postorder = [-1]
    Output: [-1]

    Constraints:
    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
    inorder is guaranteed to be the inorder traversal of the tree.
    postorder is guaranteed to be the postorder traversal of the tree.

    Array, Hash Table, Divide and Conquer, Tree, Binary Tree

    Next Greater Element I, Count Substrings That Differ by One Character, Minimum Obstacle Removal to Reach Corner
    '''
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        root, mid = TreeNode(postorder[-1]), inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return root

    def main(self):
        print(self.buildTree([9,3,15,20,7], [9,15,7,20,3]))

S = Solution()
S.main()