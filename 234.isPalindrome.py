# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

    Example 1:
    Input: head = [1,2,2,1]
    Output: true

    Example 2:
    Input: head = [1,2]
    Output: false

    Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

    Linked List, Two Pointers, Stack, Recursion

    Follow up:
    Could you do it in O(n) time and O(1) space?

    Palindrome Number, Valid Palindrome, Reverse Linked List, Maximum Twin Sum of a Linked List
    '''
    # tc: O(n) sc: O(1)
    @staticmethod
    def isPalindrome(head):
        slow = fast = head
        while fast and fast.next: #locate middle node
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow  #reverse 2nd half

        while prev and head.val == prev.val: #check for palindrome
            head = head.next
            prev = prev.next
        return not prev

    @staticmethod
    def isPalindrome1(head):
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans == ans[::-1]