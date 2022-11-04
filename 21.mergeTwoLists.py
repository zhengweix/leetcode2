# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from listNode import ListNode
class Solution:
    '''
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

    Example 1:
    https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example 2:
    Input: list1 = [], list2 = []
    Output: []

    Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

    Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

    Merge k Sorted Lists, Merge Sorted Array, Sort List, Shortest Word Distance II, Add Two Polynomials Represented as Linked Lists, Longest Common Subsequence Between Sorted Arrays
    '''
    def mergeTwoLists(self, list1, list2):
        dummy = list0 = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                list0 = list1
                list0 = list0.next
                list1 = list1.next
            else:
                list0.next = list0 = list2
                list2 = list2.next
        list0.next = list1 or list2
        return dummy.next

    def mergeTwoLists1(self, list1, list2):
        if not list1 or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
