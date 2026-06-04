class Solution:
    def maxProduct(self, number: int) -> int:
        num_str = str(number)
        if len(num_str) < 2:
            return 0 
        max1 = 0
        max2 = 0
        for char in num_str:
            digit = int(char)
            if digit > max1:
                max2 = max1  
                max1 = digit 
            elif digit > max2:
                max2 = digit
        return max1 * max2