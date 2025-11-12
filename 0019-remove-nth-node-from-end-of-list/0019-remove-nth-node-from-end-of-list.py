# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return []
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next    
        x = count - n + 1
        i = 0
        dummy = ListNode(0, head)
        temp2 = dummy
        stop = x - 1
        while temp2:
            if i == stop:
                temp2.next = temp2.next.next
                break
            i += 1
            temp2 = temp2.next        
        return dummy.next            