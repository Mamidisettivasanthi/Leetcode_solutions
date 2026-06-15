class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for digit in str(num):
            digit = int(digit)
            if num % digit == 0:
                count += 1
        return count