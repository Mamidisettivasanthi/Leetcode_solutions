class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        duplicate = -1
        missing = -1
        for i in range(1, len(nums) + 1):
            if freq.get(i, 0) == 2:
                duplicate = i
            if freq.get(i, 0) == 0:
                missing = i
        return [duplicate, missing]