from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        qu = deque()
        res = []
        qu.append(root)
        while qu:
            curr = []
            x = len(qu)
            for i in range(x):
                temp = qu.popleft()
                curr.append(temp.val)
                if temp.left is not None:
                    qu.append(temp.left)
                if temp.right is not None:
                    qu.append(temp.right)
            res.append(curr[-1])
        return res 