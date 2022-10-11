# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from listNode import ListNode
class Solution:
    '''
    Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

    Example 1:
    https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

    Example 2:
    Input: head = [], val = 1
    Output: []

    Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

    Constraints:
    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50

    Linked List, Recursion

    Remove Element, Delete Node in a Linked List, Delete the Middle Node of a Linked List
    '''
    def removeElements(self, head, val):
        dummy = node = ListNode(next=head)
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
