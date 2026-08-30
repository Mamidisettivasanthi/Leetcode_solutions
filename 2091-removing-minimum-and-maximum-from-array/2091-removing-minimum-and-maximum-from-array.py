from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Put min_index before max_index
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        # Remove both from left
        left = max_index + 1

        # Remove both from right
        right = n - min_index

        # Remove min from left and max from right
        both = (min_index + 1) + (n - max_index)

        return min(left, right, both)