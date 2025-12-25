class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a','e','i','o','u','A','E','I','O','U']
        st = []
        vo = []
        for ch in s:
            if ch in v:
                st.append('#')
                vo.append(ch)
            else:
                st.append(ch)
        if not vo: return s
        m = len(vo)
        i = 0
        j = m - 1
        while i < j:
            vo[i], vo[j] = vo[j], vo[i]
            i += 1
            j -= 1
        i = 0    
        for j in range(len(st)):
            if st[j] == '#':
                st[j] = vo[i]
                i += 1
        return "".join(st)                     