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
    Linked List, Two Pointers

    Next challenges:
    Rotate Array, Split Linked List in Parts 

    turo
    '''
    #? keywords: linked list, right rotation
    #? approach: find tail to join, break node, two pointer
    # input: head = [1,2,3,4,5]
    #        k = 2
    # output [4,5,1,2,3]
    def rotateRight(self, head, k):
        p1 = head # find tail to join
        p2 = head # find break node
        n = 1
        while p1.next:
            p1 = p1.next
            n += 1
        k = k % n
        if k == 0:
            return head
        # p1 at tail
        # find break node
        i = 0
        while p2.next and i < n-k-1:
            p2 = p2.next
            i += 1
        # p2 at break node
        ans = p2.next # new head
        p2.next = None # new tail
        p1.next = head
        return ans

    def rotateRight1(self, head, k):
        if not head:
            return head
        n, node = 0, head
        while node:
            n, node = n+1, node.next
        if k := k % n:
            fast = slow = head
            while fast.next:
                fast = fast.next
                k -= 1
                if k < 0:
                    slow = slow.next
            fast.next, slow.next, head = head, None, slow.next
        return head
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