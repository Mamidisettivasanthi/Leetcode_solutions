from typing import List
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        pair_xor = set()
        for i in range(n):
            for j in range(i + 1, n):
                pair_xor.add(nums[i] ^ nums[j])
        ans = set(nums)  # (i, i, i)
        for x in pair_xor:
            for num in nums:
                ans.add(x ^ num)
        return len(ans)