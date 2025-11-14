# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ar = []
        self.inO(root, ar)
        return ar[k-1]
    def inO(self, node: Optional[TreeNode], ar: List[int]):
        if not node:return 
        self.inO(node.left, ar)
        ar.append(node.val)
        self.inO(node.right, ar)