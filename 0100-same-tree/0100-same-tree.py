# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = self.levelOrder(p)
        b = self.levelOrder(q)
        return a == b
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        qu = deque()
        qu.append(root)
        while qu:
            no = qu.popleft()
            if no:
                res.append(no.val)
                qu.append(no.left)
                qu.append(no.right)
            else:
                res.append(None)    
        return res