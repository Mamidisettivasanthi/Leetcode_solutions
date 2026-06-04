class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                result=arr[i:j+1]
                l=len(result)
                if l%2!=0:
                    total+=sum(result)
        return total
        