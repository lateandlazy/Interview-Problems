class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i ,j):
            vis[i][j] = 2
            for a, b in direc:
                nx = i + a
                ny = j + b
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if board[nx][ny] == 'O' and vis[nx][ny] == 0:
                        dfs(nx, ny)           
        for i in range(n):
            for j in [0, m-1]:
                if vis[i][j] == 0 and board[i][j] == 'O':
                    dfs(i, j)
        for j in range(m):
            for i in [0, n-1]:
                if vis[i][j] == 0 and board[i][j] == 'O':
                    dfs(i, j)    
        for i in range(1,n-1):
            for j in range(1,m-1):
                if board[i][j] == 'O' and vis[i][j] != 2:
                    board[i][j] = 'X'
        