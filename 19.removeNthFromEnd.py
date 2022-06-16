# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

    Input: head = [1], n = 1
    Output: []

    Input: head = [1,2], n = 1
    Output: [1]

    Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

    Follow up: Could you do this in one pass?

    Next challenges:
    1721 1474 2095
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: