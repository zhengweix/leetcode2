# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
    The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

    Example 1:
    https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg
    Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    Output: 3
    Explanation: The paths that sum to 8 are shown.

    Example 2:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: 3

    Constraints:
    The number of nodes in the tree is in the range [0, 1000].
    -109 <= Node.val <= 109
    -1000 <= targetSum <= 1000

    Tree, Depth-First Search, Binary Tree
    Path Sum IV, Longest Univalue Path
    '''
    def pathSum(self, root, targetSum):
        def helper(path):
            sm = cnt = 0
            for x in path[::-1]:
                sm += x
                if sm == targetSum:
                    cnt += 1
            return cnt

        def helper2(node, path):
            if not node:
                return 0
            path += [node.val]
            return helper(path) + helper2(node.left, path) + helper2(node.right, path)

        return helper2(root, [])

    def pathSum1(self, root, targetSum):
        seen = {0: 1}
        def helper(node, prefix):
            """Return number of paths summing to target for tree rooted at node."""
            if not node:
                return 0
            prefix += node.val
            ans = seen.get(prefix - targetSum, 0)
            seen[prefix] = 1 + seen.get(prefix, 0)
            ans += fn(node.left, prefix) + fn(node.right, prefix)
            seen[prefix] -= 1
            return ans
        return helper(root, 0)

    def main(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        print(self.pathSum(root, 11))

S = Solution()
S.main()