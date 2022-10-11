# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    Given the root of a complete binary tree, return the number of the nodes in the tree.

    According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

    Design an algorithm that runs in less than O(n) time complexity.

    Example 1:
    https://assets.leetcode.com/uploads/2021/01/14/complete.jpg
    Input: root = [1,2,3,4,5,6]
    Output: 6

    Example 2:
    Input: root = []
    Output: 0

    Example 3:
    Input: root = [1]
    Output: 1

    Constraints:
    The number of nodes in the tree is in the range [0, 5 * 104].
    0 <= Node.val <= 5 * 104
    The tree is guaranteed to be complete.

    Binary Search, TreeDepth-First Search, Binary Tree

    Closest Binary Search Tree Value
    '''
    # sc: O(logn)
    def countNodes(self, root):
        def helper(node):
            '''compute its height h'''
            n = 0
            while node:
                n, node = n+1, node.left
            return n
        if not root:
            return 0
        h = helper(root)
        if helper(root.right) == h-1:
            # left subtree is perfectly balanced
            return 2**(h-1) + self.countNodes(root.right)
        else:
            # the right subtree (h-1) is perfectly balanced
            return 2**(h-2) + self.countNodes(root.left)

    def main(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        print(self.countNodes(root))

S = Solution()
S.main()
