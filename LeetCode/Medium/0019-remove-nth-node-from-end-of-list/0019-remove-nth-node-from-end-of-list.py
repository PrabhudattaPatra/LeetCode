# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) 
        dummy.next = head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        delete_pos = length - n + 1
        pre = dummy 
        curr = head

        for _ in range(delete_pos-1):
            pre = curr
            curr = curr.next
        pre.next = curr.next

        return dummy.next
