# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    Example 1:
    https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg
    Input: root = [1,2,2,3,4,4,3]
    Output: true

    Example 2:
    https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg
    Input: root = [1,2,2,null,3,null,3]
    Output: false

    Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

    Follow up:
    Could you solve it both recursively and iteratively?

    Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Inorder Successor in BST II, Build Binary Expression Tree From Infix Expression, Check If Two Expression Trees are Equivalent
    '''
    def isSymmetric(self, root):
        '''BFS iterative'''
        queue, seen = [(root, root)], []
        while queue:
            for _ in range(len(queue)):
                u, v = queue.pop(0)
                if not u and not v:
                    continue
                if not u or not v or u.val != v.val:
                    return False
                queue.append((u.left, v.right))
                queue.append((u.right, v.left))
        return True

    def isSymmetric1(self, root):
        '''DFS recursive'''
        def helper(u, v):
            if not u or not v:
                return u == v
            return u.val == v.val and helper(u.left, v.right) and helper(u.right, v.left)
        return helper(root.left, root.right)

