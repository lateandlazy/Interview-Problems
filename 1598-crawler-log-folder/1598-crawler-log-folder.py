class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for ch in logs:
            if ch == '../':
                if not st: continue
                st.pop()
            elif ch == './':
                continue
            else:       
                st.append(0)
        return len(st) 