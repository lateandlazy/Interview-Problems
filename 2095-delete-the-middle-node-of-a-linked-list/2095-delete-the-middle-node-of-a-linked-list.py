# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        f = dummy.next
        s = dummy
        while f is not None and f.next is not None:
            f = f.next.next
            s = s.next
        s.next = s.next.next
        return dummy.next    