from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        n = len(s)
        if m > n:
            return []
        p_count = Counter(p)
        window = Counter(s[:m])
        result = []
        if window == p_count:
            result.append(0)
        for i in range(m, n):
            window[s[i]] += 1
            window[s[i - m]] -= 1
            if window[s[i - m]] == 0:
                del window[s[i - m]]
            if window == p_count:
                result.append(i - m + 1)
        return result