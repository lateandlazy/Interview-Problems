class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = [0 for _ in range(n)]
        def dfs(i, vis):
            vis[i] = 1
            for j in rooms[i]:
                if vis[j] == 0:
                    dfs(j, vis)
            return        
        dfs(0, vis)
        for num in vis:
            if num == 0:
                return False
        return True 