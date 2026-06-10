from typing import List
import heapq
import math
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LOG = math.floor(math.log2(n)) + 1
        stMax = [[0] * LOG for _ in range(n)]
        stMin = [[0] * LOG for _ in range(n)]
        for i in range(n):
            stMax[i][0] = nums[i]
            stMin[i][0] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1
            for i in range(n - length + 1):
                stMax[i][j] = max(
                    stMax[i][j - 1],
                    stMax[i + half][j - 1]
                )
                stMin[i][j] = min(
                    stMin[i][j - 1],
                    stMin[i + half][j - 1]
                )
            j += 1
        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1
        def get_value(l, r):
            length = r - l + 1
            p = log[length]
            mx = max(
                stMax[l][p],
                stMax[r - (1 << p) + 1][p]
            )
            mn = min(
                stMin[l][p],
                stMin[r - (1 << p) + 1][p]
            )
            return mx - mn
        heap = []
        for l in range(n):
            val = get_value(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))
        ans = 0
        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            ans += -val
            if r > l:
                new_val = get_value(l, r - 1)
                heapq.heappush(heap, (-new_val, l, r - 1))
        return ans