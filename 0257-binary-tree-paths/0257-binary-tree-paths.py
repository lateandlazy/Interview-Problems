# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def binaryTreepaths(root, s):
            if not root.left and not root.right:
                s += str(root.val)
                res.append(s)
            s += str(root.val)
            s += '->'    
            if root.left:
                binaryTreepaths(root.left, s)  
            if root.right:
                binaryTreepaths(root.right, s)      
        s = ''         
        binaryTreepaths(root, s)
        return res