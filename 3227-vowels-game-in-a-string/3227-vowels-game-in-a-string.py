class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel = 'aeiou'
        count = 0
        for ch in s:
            if ch in vowel:
                count += 1 
        if not count : return False        
        if count ^ 1 == 0: return True
        return True
