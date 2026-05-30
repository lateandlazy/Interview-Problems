class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        unique_chars = set(word)
        cnt = 0
        for ch in unique_chars:
            if ch.islower() and ch.upper() in unique_chars:
                cnt += 1
        return cnt                           
            
        