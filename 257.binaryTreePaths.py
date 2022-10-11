# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree, return all root-to-leaf paths in any order.
    A leaf is a node with no children.

    Example 1:
    https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg
    Input: root = [1,2,3,null,5]
    Output: ["1->2->5","1->3"]

    Example 2:
    Input: root = [1]
    Output: ["1"]

    Constraints:
    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100

    String, Backtracking, Tree, Depth-First Search, Binary Tree

    Step-By-Step Directions From a Binary Tree Node to Another
    '''
    def binaryTreePaths(self, root):
        def helper(node, s):
            if not node:
                return
            if not node.left and not node.right:
                s += str(node.val)
                ans.add(s)
            else:
                s += str(node.val) + '->'
            helper(node.left, s)
            helper(node.right, s)

        ans = set()
        helper(root, '')
        return ans


