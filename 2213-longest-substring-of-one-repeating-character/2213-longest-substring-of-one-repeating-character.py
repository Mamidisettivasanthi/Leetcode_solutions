from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        size = 1

        while size < n:
            size *= 2

        tree = [None] * (2 * size)

        def create(ch):
            return [ch, ch, 1, 1, 1, 1]

        for i in range(n):
            tree[size + i] = create(s[i])

        for i in range(n, size):
            tree[size + i] = None

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            length = a[5] + b[5]
            prefix = a[2]
            suffix = b[3]
            best = max(a[4], b[4])

            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                if b[3] == b[5]:
                    suffix = b[5] + a[3]

            return [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                length
            ]

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, ch):
            i = size + pos
            tree[i] = create(ch)

            i //= 2

            while i:
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
                i //= 2

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(idx, ch)
            ans.append(tree[1][4])

        return ans