class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        ans = -1
        for num in freq:
            if num == freq[num]:
                ans = max(ans, num)
        return ans
        