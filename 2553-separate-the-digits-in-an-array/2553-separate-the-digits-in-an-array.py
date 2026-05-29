class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def Separate(num: int):
            Slist = []
            while num > 0:
                x = num % 10
                Slist.append(x)
                num = num // 10
            Slist.reverse()
            return Slist
        res = []
        for num in nums:
            temp = Separate(num)
            for x in temp:
                res.append(x)
        return res                
        