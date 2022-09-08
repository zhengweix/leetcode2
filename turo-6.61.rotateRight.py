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
    '''
    def rotateRight(self, head, k: int):
        if head == None or head.next == None or k == 0:
            return head
        n = 1
        head1 = head
        while head1.next:
            n += 1
            head1 = head1.next
        m = k%n
        if m == 0:
            return head

        l = 1
        head2 = head
        while head2.next:
            if l >= n-m:
                head3 = head2.next
                head2.next = None
                break
            else:
                head2 = head2.next
                l += 1
        head4 = head3
        while head3.next:
            head3 = head3.next
        head3.next = head
        return head4

    def main(self):
        head = ListNode(0)
        head1 = self.rotateRight(head, 0)
        if not head1.next:
            print(head1.val)
        else:
            while head1.next:
                print(head1.val)
                head1 = head1.next
            print(head1.val)

S = Solution()
S.main()