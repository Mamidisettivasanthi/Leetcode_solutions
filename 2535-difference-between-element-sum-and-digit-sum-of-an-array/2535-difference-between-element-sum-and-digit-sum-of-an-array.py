class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum=0
        element_sum=sum(nums)
        for num in nums:
            for digit in str(abs(num)):
                digit_sum += int(digit)
        return abs(element_sum-digit_sum)
        
        