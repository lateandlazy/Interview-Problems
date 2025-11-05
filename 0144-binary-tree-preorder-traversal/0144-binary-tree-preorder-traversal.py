# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.pTraversal(root, res)
        return res
    def pTraversal(self, node: Optional[TreeNode], res: List[int]) -> List[int]:
        if not node:
            return
        res.append(node.val) 
        self.pTraversal(node.left, res)
        self.pTraversal(node.right, res)
        return res   
            