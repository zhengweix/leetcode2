# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from listNode import ListNode
class Solution:
    '''
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:
    https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

    Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

    Linked List, Math, Recursion

    Multiply Strings, Sum of Two Integers, Add Two Numbers II, Add Two Polynomials Represented as Linked Lists
    '''
    # l1 = [2, 4, 3], l2 = [5, 6, 4]
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = l0 = ListNode()
        #! also consider carry after l1, l2 iteration done
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            #l0.next = l0 = ListNode(carry % 10)
            l0.next = ListNode(carry % 10)
            l0 = l0.next
            carry //= 10
        return dummy.next

    def main(self):
        l1 = ListNode()
        l11 = l1
        for val in [2,4,3]:
            l11.next = ListNode(val)
            l11 = l11.next

        l2= ListNode()
        l22 = l2
        for val in [5,6,4]:
            l22.next = ListNode(val)
            l22 = l22.next

        l0 = self.addTwoNumbers(l1.next, l2.next)
        while l0:
            print(l0.val)
            l0 = l0.next

S = Solution()
S.main()