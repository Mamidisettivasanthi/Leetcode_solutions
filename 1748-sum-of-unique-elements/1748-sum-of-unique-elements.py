class Solution:
    def sumOfUnique(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        total = 0
        for num in freq:
            if freq[num] == 1:
                total += num
        return total