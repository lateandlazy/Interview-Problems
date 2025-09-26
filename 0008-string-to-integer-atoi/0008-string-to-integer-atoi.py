class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() 
        if not s:
            return 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        if not num_str:
            return 0
        result = int(num_str) * sign
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        return result