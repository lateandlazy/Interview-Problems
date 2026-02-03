# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return None
        qu = deque()
        qu.append(root)
        s = float('-inf')
        cnt  = 0
        while qu:
            x = len(qu)
            curr = []
            cnt += 1
            for _ in range(x):
                no = qu.popleft()
                curr.append(no.val)
                if no.left != None:
                    qu.append(no.left)
                if no.right != None:
                    qu.append(no.right)
            if sum(curr) > s:
                s = sum(curr)
                res = cnt
        return res 