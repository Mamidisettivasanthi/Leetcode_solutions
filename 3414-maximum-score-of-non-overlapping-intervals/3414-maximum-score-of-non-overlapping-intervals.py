from typing import List
from functools import lru_cache
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # Store original index
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]

        # Sort by starting point
        arr.sort()

        n = len(arr)
        starts = [x[0] for x in arr]

        @lru_cache(None)
        def dp(i, count):

            # No more intervals or already selected 4
            if i == n or count == 4:
                return (0, ())

            # Option 1: skip current interval
            skip_score, skip_indices = dp(i + 1, count)

            l, r, w, original_index = arr[i]

            # First interval whose start > r
            next_i = bisect_right(starts, r)

            # Option 2: take current interval
            next_score, next_indices = dp(next_i, count + 1)

            take_score = w + next_score

            take_indices = tuple(sorted(
                (original_index,) + next_indices
            ))

            # Choose better score
            if take_score > skip_score:
                return take_score, take_indices

            if take_score < skip_score:
                return skip_score, skip_indices

            # Same score -> lexicographically smaller indices
            return skip_score, min(take_indices, skip_indices)

        return list(dp(0, 0)[1])