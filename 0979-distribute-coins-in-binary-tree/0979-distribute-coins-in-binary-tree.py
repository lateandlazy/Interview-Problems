# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        def dfs(node):
            nonlocal cnt
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            cnt += abs(l) + abs(r)
            return node.val + l + r - 1   
        dfs(root)
        return cnt