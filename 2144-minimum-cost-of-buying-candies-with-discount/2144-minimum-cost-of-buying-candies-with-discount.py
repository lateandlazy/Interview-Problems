class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        lst = cost
        lst.sort()
        n = len(lst)
        i = n % 3
        j = n // 3
        res = 0
        for _ in range(j):
            a = lst.pop()
            b = lst.pop()
            lst.pop()
            res += (a + b)
        if i == 1:
            res += lst[0]
        elif i == 2:
            res += (lst[0] + lst[1])
        else:
            res += 0
        return res