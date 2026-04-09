class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def solve(ss, ch1, ch2):
            if ch1 == 0 and ch2 == 0:
                res.append(ss)
                return   
            if ch1 > 0:
                solve(ss+'(', ch1 - 1, ch2)
            if ch2 > ch1:    
                solve(ss+')', ch1, ch2 - 1)                       
        solve('', n, n)
        return res
