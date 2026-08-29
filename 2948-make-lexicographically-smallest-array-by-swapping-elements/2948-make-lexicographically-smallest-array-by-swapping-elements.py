from typing import List

class Solution:
    def lexicographicallySmallestArray(
        self,
        nums: List[int],
        limit: int
    ) -> List[int]:

        n = len(nums)

        # (value, original index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = [0] * n

        i = 0

        while i < n:
            j = i

            # Find all values that belong to the same group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Original indices of this group
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            # Values are already sorted
            values = [arr[k][0] for k in range(i, j + 1)]

            # Put smallest values at smallest indices
            for k in range(len(indices)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans