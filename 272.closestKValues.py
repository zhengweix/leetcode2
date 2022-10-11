# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

    You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

    Example 1:
    https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg
    Input: root = [4,2,5,1,3], target = 3.714286, k = 2
    Output: [4,3]

    Example 2:
    Input: root = [1], target = 0.000000, k = 1
    Output: [1]

    Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 104.
    0 <= Node.val <= 109
    -109 <= target <= 109

    Follow up:
    Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?

    Stack, Tree, Depth-First Search, Binary Search Tree, Two Pointers, Binary Tree, Heap (Priority Queue)
    '''
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]: