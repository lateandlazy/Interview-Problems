from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        a = []
        b = []
        l = root.left
        r = root.right  
        qul = deque([root.left])
        qur = deque([root.right])
        while qul:
            curr = []
            x = len(qul)
            for _ in range(x):
                temp = qul.popleft()
                if temp is None:    
                    curr.append(None)
                    continue
                curr.append(temp.val)
                if temp.left is not None:
                    qul.append(temp.left)
                else: qul.append(None)    
                if temp.right is not None:
                    qul.append(temp.right)
                else: qul.append(None)      
            a.append(curr)
        while qur:
            curr = []
            x = len(qur)
            for _ in range(x):
                temp = qur.popleft()
                if temp is None:
                    curr.append(None)
                    continue
                curr.append(temp.val)
                if temp.left is not None:
                    qur.append(temp.left)
                else: qur.append(None)    
                if temp.right is not None:
                    qur.append(temp.right)  
                else: qur.append(None)    
            curr.reverse()
            b.append(curr)  
        if a == b: return True
        return False 