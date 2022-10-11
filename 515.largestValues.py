# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

    Example 1:
    https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg
    Input: root = [1,3,2,5,3,null,9]
    Output: [1,3,9]

    Example 2:
    Input: root = [1,2,3]
    Output: [1,3]

    Constraints:
    The number of nodes in the tree will be in the range [0, 104].
    -231 <= Node.val <= 231 - 1

    Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Count Complete Tree Nodes, Binary Tree Tilt, Smallest Common Region
    '''
    def largestValues(self, root):
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            row = []
            for _ in range(len(queue)):
                u = queue.pop(0)
                row.append(u.val)
                if u.left:
                    queue.append(u.left)
                if u.right:
                    queue.append(u.right)
            ans.append(max(row))
        return ans

    def largestValues1(self, root):
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            ans.append(max(x.val for x in queue))
            row = [x.left for x in queue if x.left] + [x.right for x in queue if x.right]
            queue = row
        return ans

    def largestValues2(self, root):
        ans = []
        if not root:
            return ans
        queue = [(root, 0)]
        while queue:
            u, i = queue.pop(0)
            if u:
                if i == len(ans):
                    ans.append(u.val)
                else:
                    ans[i] = max(ans[i], u.val)
                queue.append((u.left, i+1))
                queue.append((u.right, i+1))
        return ans

