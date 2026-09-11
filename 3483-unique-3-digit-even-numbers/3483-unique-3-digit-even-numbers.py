from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        n = len(digits)

        for i in range(n):          # units digit
            if digits[i] % 2 != 0:
                continue

            for j in range(n):      # tens digit
                if j == i:
                    continue

                for k in range(n):  # hundreds digit
                    if k == i or k == j:
                        continue

                    if digits[k] == 0:
                        continue

                    num = digits[k] * 100 + digits[j] * 10 + digits[i]
                    numbers.add(num)

        return len(numbers)