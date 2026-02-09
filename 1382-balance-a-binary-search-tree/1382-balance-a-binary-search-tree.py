# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        ar = []
        def trav(root):    
            if not root:
                return
            trav(root.left) 
            ar.append(root.val)
            trav(root.right)  
        trav(root) 
        def build(ar):
            if not ar:
                return None
            mid = len(ar) // 2
            node = TreeNode(ar[mid])
            node.left = build(ar[:mid])
            node.right = build(ar[mid+1:])
            return node    
        return build(ar) 