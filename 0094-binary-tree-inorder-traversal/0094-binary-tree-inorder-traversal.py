# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.iTraversal(root, res)
        return res
    def iTraversal(self, node: Optional[TreeNode], res: List[int]) -> List[int]:
        if node is None:
            return
        self.iTraversal(node.left, res)
        res.append(node.val) 
        self.iTraversal(node.right, res)
        return res 