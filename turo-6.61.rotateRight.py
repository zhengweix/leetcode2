from listNode import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Given the head of a linked list, rotate the list to the right by k places.

    Example 1:
    https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

    Example 2:
    https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

    Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

    Related Topics
    Linked List， Two Pointers

    Next challenges:
    Rotate Array
    Split Linked List in Parts
    '''
    def rotateRight(self, head, k: int):
        if not head or not head.next:
            return head

        n = 0
        pointer0 = head
        while pointer0:
            pointer0 = pointer0.next
            n += 1

        m = k % n
        if k == 0:
            return head

        pointer1, pointer2 = head, head
        for i in range(m):
            pointer2 = pointer2.next

        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        res = pointer1.next
        pointer1.next = None
        pointer2.next = head
        return res

    def main(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head1 = self.rotateRight(head, 2)
        while head1:
            print(head1.val)
            head1 = head1.next
S = Solution()
S.main()