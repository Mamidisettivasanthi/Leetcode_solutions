class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        target = str(x)
        return s[0] != target and target in s