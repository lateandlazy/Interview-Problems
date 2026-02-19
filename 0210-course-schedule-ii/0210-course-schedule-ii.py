class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            ar = []
            for i in range(numCourses):
                ar.append(i)
            return ar    
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        ar = []
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
            ar.append(t)
            for j in adj[t]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    qu.append(j)
        if count == numCourses:
            return ar
        return [] 