from typing import List

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check if palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        m = n // 2
        half = [x // 2 for x in cnt]

        # ------------------------------------------------
        # CASE 1: Try using exactly target's left half
        # ------------------------------------------------

        used = [0] * 26
        possible = True

        for i in range(m):
            x = ord(target[i]) - ord('a')

            used[x] += 1

            if used[x] > half[x]:
                possible = False
                break

        if possible:
            left = target[:m]

            # Construct the palindrome
            candidate = left + middle + left[::-1]

            if candidate > target:
                return candidate

        # ------------------------------------------------
        # CASE 2: Make the left half slightly larger
        # ------------------------------------------------

        for i in range(m - 1, -1, -1):

            used = [0] * 26
            possible = True

            # Match target before position i
            for j in range(i):
                x = ord(target[j]) - ord('a')

                used[x] += 1

                if used[x] > half[x]:
                    possible = False
                    break

            if not possible:
                continue

            x = ord(target[i]) - ord('a')

            # Try a larger character at position i
            for y in range(x + 1, 26):

                if used[y] >= half[y]:
                    continue

                remaining = half[:]

                # Remove prefix characters
                for c in range(26):
                    remaining[c] -= used[c]

                # Use y at position i
                remaining[y] -= 1

                left = target[:i] + chr(y + ord('a'))

                # Fill remaining positions with smallest characters
                for c in range(26):
                    left += chr(c + ord('a')) * remaining[c]

                candidate = left + middle + left[::-1]

                if candidate > target:
                    return candidate

        return ""