from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False
        x_info = None
        y_info = None    
        qu = deque([(root,None,0)])
        while qu:
            curr, parent, depth = qu.popleft()
            if curr.val == x:
                x_info = (parent, depth)
            elif curr.val == y:
                y_info = (parent, depth)
            if y_info and x_info:
                return x_info[1] == y_info[1]  and x_info[0] != y_info[0]  
            if curr.left:
                qu.append((curr.left, curr, depth + 1))
            if curr.right:
                qu.append((curr.right, curr, depth + 1))  
        return False 