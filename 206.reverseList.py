# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Input: head = [1,2]
    Output: [2,1]

    Input: head = []
    Output: []

    Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

    Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
    '''
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            head.next, head, pre = pre, head.next, head

        return pre

    def reverseList1(self, head: ListNode) -> ListNode:
        def helper(node, pre):
            if not node:
                return pre
            node.next, node, pre = pre, node.next, node
            return helper(node, pre)
        return helper(head, None)
#649 2074 2130 234