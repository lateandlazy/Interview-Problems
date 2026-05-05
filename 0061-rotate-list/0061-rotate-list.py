# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:return head
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        k = k % cnt
        if k == 0:return head
        temp1 = head
        for _ in range(cnt-k-1):
            temp1 = temp1.next
        ntemp = temp1.next
        temp1.next = None
        temp2 = ntemp
        while temp2.next:
            temp2 = temp2.next
        temp2.next = head
        return ntemp    

