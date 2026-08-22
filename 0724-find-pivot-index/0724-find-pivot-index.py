class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref=[0]*len(nums)
        pref[0]=nums[0]
        for i in range(1,len(nums)):
            pref[i]=pref[i-1]+nums[i]
        total=pref[-1]
        for i in range(len(nums)):
            left=pref[i-1] if i>0 else 0
            right=total-pref[i]
            if left==right:
                return i
        return -1
        
            
        