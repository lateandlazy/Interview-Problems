class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        op = ''
        ar = []
        self.solve(s,op,ar)
        return ar
    def solve(self, ip: str, op: str, ar: List[str]) -> List[str]:
        if len(ip) == 0:
            ar.append(op)
            return
        while ip[0].isdigit():
            op += ip[0]
            ip = ip[1:]
            if not ip:
                ar.append(op)
                return
        op1 = op
        op2 = op
        op1 += ip[0].lower()
        op2 += ip[0].upper()
        ip = ip[1:]
        self.solve(ip,op1,ar)
        self.solve(ip,op2,ar)        
