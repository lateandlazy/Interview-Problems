class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        temp = self.solve(n,k)
        if temp == 0 or temp == False:
            return 0
        else: return 1     
    def solve(self, n: int, k: int) -> int: 
        if n == 1 and k == 1:
            return 0
        elif n == 1 and k > 1:
            return 1    
        else:
            mid = (2 ** (n-1)) // 2
            if k <= mid:
                return self.kthGrammar(n-1,k)
            else:
                return not self.kthGrammar(n-1,k-mid)            