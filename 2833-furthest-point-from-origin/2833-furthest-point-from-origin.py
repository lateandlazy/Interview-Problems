class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        either = 0
        for ch in moves:
            if ch == 'L':left += 1
            elif ch == 'R':right += 1
            else:either += 1
        return abs(left - right) + either