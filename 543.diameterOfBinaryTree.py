# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges between them.

    Example 1:
    https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

    Example 2:
    Input: root = [1,2]
    Output: 1

    Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100

    Tree, Depth-First Search, Binary Tree

    Diameter of N-Ary Tree, Longest Path With Different Adjacent Characters
    '''
    def diameterOfBinaryTree(self, root):
        def helper(node):
            nonlocal ans
            if not node:
                return 0
            left, right = helper(node.left), helper(node.right)
            ans = max(ans,  left + right + 1)
            return max(left, right) + 1

        ans = 0
        helper(root)
        return ans

    def main(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        print(self.diameterOfBinaryTree(root))

S = Solution()
S.main()