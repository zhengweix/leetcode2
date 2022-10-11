# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
from heapq import *
from collections import *
class Solution:
    '''
    Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

    Example 1:
    https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg
    Input: root = [3,1,4,null,2], k = 1
    Output: 1

    Example 2:
    https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

    Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104

    Follow up:
    If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
    '''
    def kthSmallest(self, root, k):
        '''inorder traversal to collect numbers in tree'''
        def helper(node):
            if not node:
                return
            helper(node.left)
            heappush(ans, -node.val)
            if len(ans) > k:
                heappop(ans)
            helper(node.right)
        ans = []
        helper(root)
        return -sorted(ans)[0]

    def kthSmallest1(self, root, k):
        ''' BST check the most left nodes fist then to right side stored in stack '''
        node, stack = root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right

    def kthSmallest2(self, root, k):
        ''' Follow up For each node, use extra space to save (number of nodes in left subtree) '''
        cache = defaultdict(TreeNode)
        def helper(node):
            '''build up cache'''
            if not node:
                return 0
            cache[node] = helper(node.left) + helper(node.right) + 1
            return cache[node]

        def helper1(node, k):
            '''search the cache to locate k'''
            if node.left:
                if k <= cache[node.left]:
                    return helper1(node.left, k)
                else:
                    k -= cache[node.left]
            if k == 1:
                return node.val
            return helper1(node.right, k-1)

        helper(root)
        return helper1(root, k)

    def main(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        print(self.kthSmallest(root, 6))

S = Solution()
S.main()