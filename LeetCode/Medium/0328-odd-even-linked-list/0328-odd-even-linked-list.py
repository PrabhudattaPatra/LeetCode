# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        c1 = head
        c2 = head.next

        temp = c2

        while c2 and c2.next:
            c1.next = c2.next
            c1 = c1.next
            c2.next = c1.next
            c2 = c2.next
        
        c1.next = temp
        return head