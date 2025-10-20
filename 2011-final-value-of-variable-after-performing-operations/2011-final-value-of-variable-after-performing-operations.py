class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        ans = 0
        for x in op:
            for ch in x:
                if ch == '+':
                    ans += 1
                    break
                if ch == '-':
                    ans -= 1
                    break
        return ans                