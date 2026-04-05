class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up = 0
        down = 0
        r = 0
        l = 0
        for ch in moves:
            if ch == 'R': r += 1
            elif ch == 'L': l += 1
            elif ch == 'U': up += 1
            else: down += 1
        return up == down and r == l 