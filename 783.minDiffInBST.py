class Solution:
    '''
    Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

    Example 1:
    https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg
    Input: root = [4,2,6,1,3]
    Output: 1

    Example 2:
    https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

    Constraints:
    The number of nodes in the tree is in the range [2, 100].
    0 <= Node.val <= 105

    Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree

    Surrounded Regions, Binary Tree Longest Consecutive Sequence, Count Servers that Communicate
    '''
    def minDiffInBST(self, root):
        ans, prev = inf, None
        def helper(node):
            '''inorder depth-first traversal (recursive)'''
            nonlocal ans, prev
            if not node:
                return
            helper(node.left)
            if prev is not None:
                ans = min(ans, abs(node.val - prev))
            prev = node.val
            helper(node.right)
        helper(root)
        return ans
