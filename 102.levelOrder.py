# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Input: root = [1]
    Output: [[1]]

    Input: root = []
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000

    Next challenges:
    103 107 651 637 993 429
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        queue = [root]
        while queue:
            i, n, result = 0, len(queue), []
            while i < n:
                u = queue.pop(0)
                result.append(u.val)
                if u.left:
                    queue.append(u.left)
                if u.right:
                    queue.append(u.right)
                i += 1
            results.append(result)
        return results

    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root, queue, level):
            if root is None:
                return queue

            if level not in queue:
                queue[level] = []

            queue[level].append(root.val)
            if root.left:
                helper(root.left, queue, level + 1)

            if root.right:
                helper(root.right, queue, level + 1)

            return queue

        queue = helper(root, {}, 0)
        return [queue[level] for level in queue]