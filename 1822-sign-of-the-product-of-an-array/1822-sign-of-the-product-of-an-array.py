class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result=1
        for i in range(len(nums)):
            if nums[i]>0:
                product=1
                result=result*product
                i=i+1
            elif nums[i]<0:
                product=-1
                result=result*product
                i=i+1
            else:
                result=0
        return result
        