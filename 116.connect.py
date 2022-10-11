"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    '''
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
    Initially, all next pointers are set to NULL.

    Example 1:
    https://assets.leetcode.com/uploads/2019/02/14/116_sample.png
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]
    Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

    Example 2:
    Input: root = []
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 212 - 1].
    -1000 <= Node.val <= 1000

    Follow-up:
    You may only use constant extra space.
    The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

    Populating Next Right Pointers in Each Node II, Binary Tree Right Side View
    '''
    # tc: O(n) sc: O(n)
    def connect(self, root):
        if not root:
            return None
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                u = queue.pop(0)
                if i < size - 1:
                    u.next = queue[0]
                if u.left:
                    queue.append(u.left)
                if u.right:
                    queue.append(u.right)
        return root

    # tc: O(n) sc: O(1)
    def connect1(self, root):
        node = root
        while node and node.left:
            node1 = node
            while node1:
                node1.left.next = node1.right
                if node1.next:
                    node1.right.next = node1.next.left
                node1 = node1.next
            node = node.left
        return root