from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        check = True
        if root is None:
            return res
        qu = deque()
        qu.append(root)
        while qu:
            x = len(qu)
            curr = []
            for _ in range(x):
                temp = qu.popleft()
                curr.append(temp.val)
                if temp.left is not None:
                    qu.append(temp.left)
                if temp.right is not None:
                    qu.append(temp.right) 
            if check == True:
                res.append(curr)
            else:
                curr.reverse()
                res.append(curr)
            check = not check
        return res 