# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        qu = deque()
        qu.append(root)
        while qu:
            x = len(qu)
            curr = []
            for _ in range(x):
                no = qu.popleft()
                curr.append(no.val)
                if no.left != None:
                    qu.append(no.left)
                if no.right != None:
                    qu.append(no.right)
            res.append(curr)
        res.reverse()
        return res