# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head
        while r is not None and r.next is not None:
            l = l.next
            r = r.next.next
        return l 