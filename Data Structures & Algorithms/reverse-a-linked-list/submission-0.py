# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr=head
            nxt=curr.next
            prev=None
            while nxt is not None:
                curr.next=prev
                prev=curr
                curr=nxt
                nxt=curr.next
            curr.next=prev
            return curr
        else:
            return head