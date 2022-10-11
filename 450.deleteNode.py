# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from treeNode import TreeNode
class Solution:
    '''
    Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
    Basically, the deletion can be divided into two stages:
    Search for a node to remove.
    If the node is found, delete the node.

    Example 1:
    https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg
    Input: root = [5,3,6,2,4,null,7], key = 3
    Output: [5,4,6,2,null,null,7]
    Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
    One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
    Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
    https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg

    Example 2:
    Input: root = [5,3,6,2,4,null,7], key = 0
    Output: [5,3,6,2,4,null,7]
    Explanation: The tree does not contain a node with value = 0.

    Example 3:
    Input: root = [], key = 0
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -105 <= Node.val <= 105
    Each node has a unique value.
    root is a valid binary search tree.
    -105 <= key <= 105

    Follow up:
    Could you solve it with time complexity O(height of tree)?

    Tree, Binary Search Tree, Binary Tree

    Split BST
    '''
    def deleteNode(self, root, key):
        if root: #locating the node to remove
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            else: # deleting node in variable cases
                if not root.left or not root.right: #Node to be deleted is the leaf or has only one child
                    return root.left or root.right
                node = root.right # Node to be deleted has two children
                while node.left: # find inorder successor of the node (smallest node on right side)
                    node = node.left
                root.val = node.val # copy value of the inorder successor to the node
                root.right = self.deleteNode(root.right, node.val) # delete the inorder successor
        return root

    def main(self):
        root = TreeNode(50)
        root.left = TreeNode(30)
        root.right = TreeNode(70)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(40)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(80)
        root.right.left.left = TreeNode(55)
        root1 = self.deleteNode(root, 50)
        print(root1.right.val)
        print(root1.right.left.val)
        print(root1.right.right.val)

S = Solution()
S.main()