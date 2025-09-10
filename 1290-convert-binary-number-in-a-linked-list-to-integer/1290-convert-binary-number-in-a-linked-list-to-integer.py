# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        cc = ''
        while temp:
            new = temp.val
            cc += str(new)
            temp = temp.next
        ans = int(cc, 2)
        return ans    
