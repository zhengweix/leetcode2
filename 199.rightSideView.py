# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    Example 1:
    https://assets.leetcode.com/uploads/2021/02/14/tree.jpg
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

    Example 2:
    Input: root = [1,null,3]
    Output: [1,3]

    Example 3:

    Input: root = []
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

    Boundary of Binary Tree
    '''
    def rightSideView(self, root):
        def helper(node, lmt):
            if not node:
                return
            if lmt > len(ans):
                ans.append(node.val)
            helper(node.right, lmt+1) or helper(node.left, lmt+1)
        ans = []
        helper(root, 0)
        return ans

