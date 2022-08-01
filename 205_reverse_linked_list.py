'''
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Solution:
___________

Take the old-school 3 pointer iterative approach. 
p = Null
q = head
r = head->next
switch the links in a loop and keep on moving the pointers one link ahead
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Iterative Approach
        q = head 
        p = None
        while q:
            # swtich the link
            r = q.next 
            q.next = p
            # move the pointers by one
            p = q
            q = r
        return p
