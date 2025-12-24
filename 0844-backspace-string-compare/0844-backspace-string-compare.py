class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []
        n = len(s)
        m = len(t)
        for i in range(n):
            if s[i] == '#':
                if not st1: continue
                st1.pop()
            else:
                st1.append(s[i])
        for i in range(m):
            if t[i] == '#':
                if not st2: continue
                st2.pop()
            else:
                st2.append(t[i])
        a = "".join(st1)
        b = "".join(st2)
        return a == b