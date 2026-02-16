class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [0 for _ in range(n)]
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        def dfs(m):
            vis[m] = 1
            for a in adj[m]:
                if vis[a] == 0:
                    dfs(a)
            return        
        cnt = 0    
        for i in range(n):
            if vis[i] == 0:
                dfs(i)  
                cnt += 1   
        return cnt 