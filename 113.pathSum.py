# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
    A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

    Example 1:
    https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]
    Explanation: There are two paths whose sum equals targetSum:
    5 + 4 + 11 + 2 = 22
    5 + 8 + 4 + 5 = 22

    Example 2:
    https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg
    Input: root = [1,2,3], targetSum = 5
    Output: []

    Example 3:
    Input: root = [1,2], targetSum = 0
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

    Backtracking, Tree, Depth-First Search, Binary Tree

    Binary Tree Paths, Path Sum III, Path Sum IV, Step-By-Step Directions From a Binary Tree Node to Another
    '''
    def pathSum(self, root, targetSum):
        # DFS through the tree
        def helper(node, sm, path):
            # If there isn't a node, return empty list
            if not node:
                print(path)
                return []
            # Add current node into the sum and path
            sm, path = sm + node.val, path + [node.val]
            # If there is no child node
            if not node.left and not node.right:
                # Return the path if sum is equal to target sum else return empty list
                return [path] if sm == targetSum else []
            #! Else, go to child nodes
            return helper(node.left, sm, path) + helper(node.right, sm, path)
        return helper(root, 0, [])

    def pathSum1(self, root, targetSum):
        def helper(node, sm, path, paths):
            if not node:
                return
            path.append(node.val)
            if node.val == sm and not node.left and not node.right:
                #! take care of deep copying
                paths.append(path[:])
            else:
                helper(node.left, sm - node.val, path, paths)
                helper(node.right, sm - node.val, path, paths)
            del path[-1]

        paths = []
        helper(root, targetSum, [], paths)
        return paths

    def main(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        print(self.pathSum(root, 9))

S = Solution()
S.main()