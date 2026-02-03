# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
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
            res.append(max(curr))
        return res 