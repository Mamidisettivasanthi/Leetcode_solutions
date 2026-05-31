class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        for value in dict.values():
            if value >= 2:
                return True
        return False

        