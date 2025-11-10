import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head.next
        while r is not None:
            a = math.gcd(l.val, r.val)
            x = ListNode(a)
            l.next = x
            x.next = r
            l = r
            r = r.next
        return head 