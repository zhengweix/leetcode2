# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from listNode import ListNode
class Solution:
    '''
    Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
    Do not modify the linked list.

    Example 1:
    https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

    Example 2:
    https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

    Example 3:
    https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

    Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

    Follow up:
    Can you solve it using O(1) (i.e. constant) memory?

    Hash Table, Linked List, Two Pointers

    Number of Matching Subsequences, X of a Kind in a Deck of Cards, Group the People Given the Group Size They Belong To
    '''
    def detectCycle1(self, head: ListNode) -> ListNode:
        def helper(node, dict):
            if node in dict:
                return node
            dict[node] = True
            if node.next:
                return helper(node.next, dict)
            return None
        if head is None:
            return None
        return helper(head, {})

    #? When fast and slow meet, the num of steps form head to start equals slow to start.
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    slow = slow.next
                    head = head.next
                return slow
        return None

    def main(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(6)
        head.next.next.next.next.next.next = head.next.next
        print(self.detectCycle1(head).val)

S = Solution()
S.main()