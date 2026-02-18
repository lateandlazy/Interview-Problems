class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            inDegree[a] += 1
        qu = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                qu.append(i)
        count = 0        
        while qu:
            t = qu.popleft()
            count += 1
            for j in adj[t]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    qu.append(j)
        if count == numCourses:
            return True
        return False 