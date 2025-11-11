# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = self.solve(root)
        return height
    def solve(self, node: Optional[TreeNode]) -> int:  
        if not node: return 0
        l = self.solve(node.left)
        r = self.solve(node.right)
        return max(l, r) + 1