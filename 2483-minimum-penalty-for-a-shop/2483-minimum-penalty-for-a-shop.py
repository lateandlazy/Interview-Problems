class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre = [0] * n
        s = 0
        for i in range(n):
            if customers[i] == 'N':
                s += 1
            pre[i] = s   
        post = [0] * n
        s = 0
        for i in range(n-1, -1, -1):
            if customers[i] == 'Y':
                s += 1
            post[i] = s
        curr = post[0]
        min_pen = curr
        h = 0
        for i in range(1,n):
            curr = pre[i-1] + post[i]
            if curr < min_pen:
                min_pen = curr
                h = i
        if pre[n-1] < min_pen:
            h = n        
        return h                   
