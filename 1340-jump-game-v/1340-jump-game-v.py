from typing import List
from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dfs(i):
            best = 1

            # Jump left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break

                best = max(best, 1 + dfs(j))

            # Jump right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break

                best = max(best, 1 + dfs(j))

            return best

        ans = 0

        for i in range(n):
            ans = max(ans, dfs(i))

        return ans