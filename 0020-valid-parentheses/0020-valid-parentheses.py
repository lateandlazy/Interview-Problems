class Solution:
    def isValid(self, s: str) -> bool:
        stack = ''
        for a in s:
            if a == '(':
                stack += ')'
            elif a == '[':
                stack += ']'
            elif a == '{':
                stack += '}'
            else:
                if not stack or a != stack[-1]:
                    return False
                stack = stack[:-1]
        return len(stack) == 0                    
