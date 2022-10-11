# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree.
    We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

    Example 1:
    https://assets.leetcode.com/uploads/2019/12/18/leetcode_testcase_1.png
    Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
    Output: true
    Explanation:
    The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
    Other valid sequences are:
    0 -> 1 -> 1 -> 0
    0 -> 0 -> 0

    Example 2:
    https://assets.leetcode.com/uploads/2019/12/18/leetcode_testcase_2.png
    Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
    Output: false
    Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

    Example 3:
    https://assets.leetcode.com/uploads/2019/12/18/leetcode_testcase_3.png
    Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
    Output: false
    Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.

    Constraints:
    1 <= arr.length <= 5000
    0 <= arr[i] <= 9
    Each node's value is between [0 - 9].

    Tree, Depth-First Search, Breadth-First Search, Binary Tree
    '''
    def isValidSequence(self, root, arr):
        def helper(node, seq):
            if not node:
                return False
            seq.append(node.val)
            if not node.left and not node.right:
                return seq == arr
            return helper(node.left, seq[:]) or helper(node.right, seq[:])

        return helper(root, [])

    def main(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)
        print(self.isValidSequence(root, [1, 1, 6]))

S = Solution()
S.main()