# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    class Solution:
        def detectCycle(self, head: ListNode) -> ListNode:
            if head is None:
                return None
            return self.detectCycleRec(head, {})

        def detectCycleRec(self, node, dict):
            if node in dict:
                return node
            dict[node] = True
            if node.next:
                return self.detectCycleRec(node.next, dict)
            return None
