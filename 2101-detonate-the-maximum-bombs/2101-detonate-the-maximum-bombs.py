class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        for i in range(n):
            x1, y1, r1 =  bombs[i]
            for j in range(n):
                if i == j: continue
                x2, y2, r2 = bombs[j]
                ds = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if ds <= r1 ** 2:
                    adj[i].append(j)
        def dfs(i, vis):
            vis[i] = 1
            count = 1
            for x in adj[i]:
                if vis[x] == 0:
                    count += dfs(x, vis)
            return count        
        res = 0
        for i in range(n):
            vis = [0] * n
            t = dfs(i, vis)
            res = max(res, t)
        return res 