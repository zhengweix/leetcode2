# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import *
from treeNode import *
class Solution:
    '''
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

    Example 1:
    https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

    Example 2:
    Input: root = [1]
    Output: [[1]]

    Example 3:
    Input: root = []
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

    Tree, Breadth-First Search, Binary Tree

    Balanced Binary Tree, Find Bottom Left Tree Value, Encode N-ary Tree to Binary Tree
    '''
    def zigzagLevelOrder(self, root):
        ans, flag = [], False
        if root:
            queue = [root]
            while queue:
                res = []
                for _ in range(len(queue)):
                    u = queue.pop(0)
                    res.append(u.val)
                    if u.left:
                        queue.append(u.left)
                    if u.right:
                        queue.append(u.right)
                ans.append(res[::-1] if flag else res)
                flag = not flag
        return ans

    def main(self):
        root = treeNode(12)
        root.left = treeNode(7)
        root.right = treeNode(1)
        root.left.left = treeNode(9)
        root.right.left = treeNode(10)
        root.right.right = treeNode(5)
        print(self.zigzagLevelOrder(root))

S = Solution()
S.main()