class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_len = 1
        count = 9
        start = 1
        while n > digit_len * count:
            n -= digit_len * count
            digit_len += 1
            count *= 10
            start *= 10
        number = start + (n - 1) // digit_len
        return int(str(number)[(n - 1) % digit_len])