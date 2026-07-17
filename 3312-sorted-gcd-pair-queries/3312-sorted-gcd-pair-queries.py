from typing import List
from collections import Counter
from itertools import accumulate
from bisect import bisect_right
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = Counter(nums)
        cnt_g = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            total = 0
            for multiple in range(g, mx + 1, g):
                total += freq[multiple]
                cnt_g[g] -= cnt_g[multiple]
            cnt_g[g] += total * (total - 1) // 2
        prefix = list(accumulate(cnt_g))
        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))
        return ans