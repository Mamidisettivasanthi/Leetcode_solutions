class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for char in s:
            freq[char]=freq.get(char,0)+1
        if len(set(freq.values()))==1:
            return True
        return False
      
        