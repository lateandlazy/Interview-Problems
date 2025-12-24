class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort()
        i = 0
        while s > 0:
            x = capacity.pop()
            s -= x
            i += 1
        return i    