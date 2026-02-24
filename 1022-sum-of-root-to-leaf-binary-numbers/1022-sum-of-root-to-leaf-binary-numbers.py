# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = []
        def dfs(node,s):
            if not node:
                return
            s += str(node.val)
            if not node.left and not node.right:
                res.append(s)
                return
            dfs(node.left, s)
            dfs(node.right,s)
        s = ''    
        dfs(root,s) 
        ans = 0
        for st in res:
            ans += int(st,2)
        return ans 