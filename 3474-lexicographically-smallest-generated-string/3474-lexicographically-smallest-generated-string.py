class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        ld = [0] * (m + n - 1)
        lt = ['*'] * (m + n - 1)
        for i in range(n):
            if str1[i] == 'T':
                temp = i
                for j in range(m):
                    if ld[temp] == 1 and lt[temp] != str2[j]:
                        return ""
                    lt[temp] = str2[j]
                    ld[temp] = 1
                    temp += 1
        oldlt = lt
        lt = ['a' if c == '*' else c for c in lt]            
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(lt[i:i+m]) != str2:
                    continue
                for j in range(i+m-1, i-1, -1):
                    if oldlt[j] == '*':
                        lt[j] = 'b'
                        break
                else:
                    return ""
        return ''.join(lt)                        


                    
