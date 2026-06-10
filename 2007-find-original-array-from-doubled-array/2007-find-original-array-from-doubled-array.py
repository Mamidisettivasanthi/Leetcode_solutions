from collections import Counter
from typing import List
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        freq = Counter(changed)
        original = []
        for num in sorted(freq.keys()):
            if freq[num] > freq[2 * num]:
                return []
            if num == 0:
                if freq[num] % 2:
                    return []
                original.extend([0] * (freq[num] // 2))
            else:
                original.extend([num] * freq[num])
                freq[2 * num] -= freq[num]
        return original