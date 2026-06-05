class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        result = []
        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]
        remaining = []
        for num in freq:
            remaining.extend([num] * freq[num])
        result.extend(sorted(remaining))
        return result


        