class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        result = []
        for num in freq:
            if freq[num] > len(nums) // 3:
                result.append(num)
        return result

        