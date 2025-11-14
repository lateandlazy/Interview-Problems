# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float('inf'), float('-inf'))
    def check(self, node: Optional[TreeNode], max_val: int, min_val: int) -> bool:
        if not node :return True
        if not(min_val < node.val < max_val): return False
        l = self.check(node.left, node.val, min_val)
        r = self.check(node.right, max_val, node.val)
        return l and r