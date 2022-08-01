'''
https://leetcode.com/problems/linked-list-cycle-ii/
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed).
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Solution:
__________

if slow and fast pointers meet at some point, then there is a loop.
Once cycle is detected, break out of the while-loop.

Now, use both pointers as slow pointers while mark one of them to start from the head of the list.
Keep moving both the pointers while they meet at some node. That node is the result.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None) or (head.next.next == None):
            return None

        p = q = head

        while q.next :
            if p.next:
                p = p.next
            if q.next.next :
                q = q.next.next
            if p == q:
                break
        # Corner Scenarios when p == q not found, and there is no cycle. hence.
        if q.next == None or q.next.next == None:
            return None
        # if p==q then start from the beginning and see where the two pointers meet
        p = head
        while p != q:
            p = p.next
            q = q.next
        return p
        
