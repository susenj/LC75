'''
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
 
Solution: 
_____________

Use two new nodes which point to null.
1. Dummy – Keep the head pointer of the resultant list
2. Curr – The new head pointer of the resultant list which will move further.

While both of the lists exist:
	If list1.next <= list2.next
	  curr.next = list1
	  list1 = list1.next
  else:
    curr.next = list2
    list2 = list2.next
  curr = curr.next
Till this point, at least one of the lists is exhausted.
So, we just need to pick the remaining portion of the non-finished list(because it's already sorted)
Once, this is done, return the dummy.next pointer. dummy pointer will contain zero..so dummy.next will
have the head of the resultant list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #print (list1.val)
        #print (list2.next.val)
        #newptr = list2
        curr = dummy = ListNode()
        
        while list1 and list2:
            if list2.val >= list1.val:
                curr.next = list1
                list1 = list1.next                
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next
