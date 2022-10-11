# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
    Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
    As a reminder, any shorter prefix of a string is lexicographically smaller.
    For example, "ab" is lexicographically smaller than "aba".
    A leaf of a node is a node that has no children.

    Example 1:
    https://assets.leetcode.com/uploads/2019/01/30/tree1.png
    Input: root = [0,1,2,3,4,3,4]
    Output: "dba"

    Example 2:
    https://assets.leetcode.com/uploads/2019/01/30/tree2.png
    Input: root = [25,1,3,1,3,0,2]
    Output: "adz"

    Example 3:
    https://assets.leetcode.com/uploads/2019/02/01/tree3.png
    Input: root = [2,2,1,null,1,0,null,0]
    Output: "abc"

    Constraints:
    The number of nodes in the tree is in the range [1, 8500].
    0 <= Node.val <= 25

    String, Tree, Depth-First Search, Binary Tree

    Binary Tree Paths
    '''
    # tc: O(n), sc: O(n)
    def smallestFromLeaf(self, root):
        def helper(node, s):
            if not node:
                return
            s = chr(node.val + 97) + s
            if not node.left and not node.right:
                ans.append(s)
            else:
                helper(node.left, s)
                helper(node.right, s)
        if not root:
            return ''
        ans = []
        helper(root, '')
        return min(ans)

    def main(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        print(self.smallestFromLeaf(root))

S = Solution()
S.main()