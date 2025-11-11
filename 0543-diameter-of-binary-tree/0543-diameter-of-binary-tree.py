# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        ans = self.height(root)
        return self.diameter
    def height(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        l = self.height(node.left)
        r = self.height(node.right)
        d = l + r
        self.diameter = max(self.diameter, d)
        return max(l, r) + 1 