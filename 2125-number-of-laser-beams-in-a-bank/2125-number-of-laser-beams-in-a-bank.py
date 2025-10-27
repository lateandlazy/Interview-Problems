class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)
        if n == 1:return 0
        prev = 0
        ans = 0
        for i in range(n):
            curr = 0
            for j in bank[i]:
                if j == '1':
                    curr += 1
            ans += (prev * curr)        
            if curr != 0:
                prev = curr
        return ans