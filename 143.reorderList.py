# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from listNode import *
class Solution:
    '''
    You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

    Example 1:
    https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

    Example 2:
    https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

    Constraints:
    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000

    Linked List, Two Pointers, Stack, Recursion

    Delete the Middle Node of a Linked List
    '''
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow

        while prev and prev.next:
            head.next, head = prev, head.next
            prev.next, prev = head, prev.next


    def main(self):
        head = ListNode(2)
        head.next = ListNode(4)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(8)
        head.next.next.next.next = ListNode(10)
        head.next.next.next.next.next = ListNode(12)
        self.reorderList(head)
        while head:
            print(head.val)
            head = head.next

S = Solution()
S.main()