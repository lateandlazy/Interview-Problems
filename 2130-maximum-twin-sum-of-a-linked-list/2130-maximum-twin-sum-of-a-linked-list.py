# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ar = []
        cur = head
        while cur:
            ar.append(cur.val)
            cur = cur.next
        res = 0
        n = len(ar)
        for i in range(n//2):
            temp = ar[i] + ar[n-i-1]
            res = max(res, temp)
        return res 