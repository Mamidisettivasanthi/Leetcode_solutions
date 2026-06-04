class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        for char in str(abs(n)):
            digit = int(char) 
            digit_sum += digit
            digit_product *= digit 
        combined_total = digit_sum + digit_product
        if combined_total == 0:
            return False
        return n % combined_total == 0
        