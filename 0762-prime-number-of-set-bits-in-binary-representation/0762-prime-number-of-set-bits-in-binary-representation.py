class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def count(n):
            cnt = 0
            while(n):
                n &= (n - 1)
                cnt += 1
            return cnt
        def check(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True
        res = 0    
        for x in range(left, right+1):
            temp = count(x)
            if check(temp):
                res += 1
        return res   