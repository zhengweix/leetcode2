from treeNode import treeNode
# Definition for a binary tree node.
# class treeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    Note: A leaf is a node with no children.
    Example 1:
    https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg
    Input: root = [3,9,20,null,null,15,7]
    Output: 2

    Example 2:
    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5

    Constraints:
    The number of nodes in the tree is in the range [0, 10^5].
    -1000 <= Node.val <= 1000

    Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Next challenges:
    510 666 426
    '''
    def minDepth(self, root):
        def helper(node):
            if not node:
                return 0
            if node.left and node.right:
                return 1 + min(helper(node.left), helper(node.right))
            else:
                return 1 + helper(node.right) + helper(node.left)
        return helper(root)

    #* add the smaller one of the child depths - except if that's zero, then add the larger one.
    def minDepth1(self, root):
        if not root:
            return 0
        ans = self.minDepth(root.left), self.minDepth(root.right)
        return 1 + (min(ans) or max(ans))

    def minDepth2(self, root):
        ans = 0
        if not root:
            return ans
        queue = [root]
        ans += 1
        while queue:
            for i in range(len(queue)):
                u = queue.pop(0)
                if u.left is None and u.right is None:
                    return ans

                if u.left:
                    queue.append(u.left)
                if u.right:
                    queue.append(u.right)
            ans += 1
        return ans

    def main(self):
        root = treeNode(3)
        root.left = treeNode(9)
        root.right = treeNode(20)
        root.right.left = treeNode(15)
        root.right.right = treeNode(7)
        print(self.minDepth1(root))

S = Solution()
S.main()