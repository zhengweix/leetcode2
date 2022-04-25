# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queues = [[root]]
        lists = []
        while queues:
            list = []
            queue = queues.pop(0)
            queue1 = []
            while queue:
                node = queue.pop(0)
                list.append(node.val)
                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
            if queue1:
                queues.append(queue1)
            if list:
                lists.append(list)

        return lists


