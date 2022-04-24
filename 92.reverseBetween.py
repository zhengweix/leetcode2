# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left >= right:
            return head

        i = 0
        pre, cur = None, head
        while cur and i < left - 1:
            pre = cur
            cur = cur.next
            i += 1

        nleft = pre
        nright = cur
        i = 0
        while cur and i < right - left + 1:
            cur.next, cur, pre = pre, cur.next, cur
            i += 1

        if nleft:
            nleft.next = pre
        else:
            head = pre

        nright.next = cur
        return head
