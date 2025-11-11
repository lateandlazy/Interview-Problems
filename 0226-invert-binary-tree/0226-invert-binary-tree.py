# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.solve(root)
        return root
    def solve(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node: return
        self.solve(node.left)
        self.solve(node.right)
        #temp = TreeNode()
        temp = node.left
        node.left = node.right
        node.right = temp
        return node    