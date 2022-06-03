# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Next challenges:
    1026 1905 2128
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(node, lst):
            if node:
                lst.append(node.val)
                if node.left:
                    helper(node.left, lst)
                else:
                    helper(None, lst)
                if node.right:
                    helper(node.right, lst)
                else:
                    helper(None, lst)
            else:
                lst.append(None)

        l1, l2 = [], []
        helper(p, l1)
        helper(q, l2)
        return l1 == l2