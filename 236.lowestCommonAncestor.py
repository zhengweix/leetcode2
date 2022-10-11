# Definition for a binary tree node.
# class TreeTreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from treeNode import TreeNode
class Solution:
    '''
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Example 1:
    https://assets.leetcode.com/uploads/2018/12/14/binarytree.png
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

    Example 2:
    https://assets.leetcode.com/uploads/2018/12/14/binarytree.png
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

    Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

    Constraints:
    The number of nodes in the tree is in the range [2, 105].
    -109 <= TreeNode.val <= 109
    All TreeNode.val are unique.
    p != q
    p and q will exist in the tree.

    Tree, Depth-First Search, Binary Tree

    Smallest Common Region, Find Players With Zero or One Losses, Lowest Common Ancestor of a Binary Tree II, Lowest Common Ancestor of a Binary Tree III, Lowest Common Ancestor of a Binary Tree IV, Step-By-Step Directions From a Binary Tree Node to Another
    '''
    def lowestCommonAncestor(self, root, p, q):
        def helper(node):
            if not node or node in (p, q):
                return node
            left, right = helper(node.left), helper(node.right)
            return node if left and right else left or right
        return helper(root)

    def main(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        print(self.lowestCommonAncestor(root, 4, 5).val)

S = Solution()
S.main()