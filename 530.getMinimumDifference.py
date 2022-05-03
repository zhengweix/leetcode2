# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        queue = [root]
        vals = [root.val]
        diff = 10**5+1
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                vals.append(node.left.val)

            if node.right:
                queue.append(node.right)
                vals.append(node.right.val)
        vals = sorted(vals)
        for i in range(1, len(vals)):
            diff = min(diff, abs(vals[i] - vals[i-1]))

        return diff
#532