class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        size = 2 * m

        # Initial vector for length = 1
        # First m states: last comparison expected DOWN
        # Next m states: last comparison expected UP
        vec = [1] * size

        # Build transition matrix
        T = [[0] * size for _ in range(size)]

        # State:
        # 0..m-1      : next comparison must be DOWN
        # m..2m-1     : next comparison must be UP

        for x in range(m):
            # From UP state -> next must go DOWN
            for y in range(x + 1, m):
                T[x][m + y] = 1

            # From DOWN state -> next must go UP
            for y in range(x):
                T[m + x][y] = 1

        def mat_mul(A, B):
            rows = len(A)
            cols = len(B[0])
            mid = len(B)

            C = [[0] * cols for _ in range(rows)]

            for i in range(rows):
                for k in range(mid):
                    if A[i][k]:
                        for j in range(cols):
                            C[i][j] = (C[i][j] +
                                       A[i][k] * B[k][j]) % MOD
            return C

        def mat_pow(M, p):
            res = [[1 if i == j else 0 for j in range(size)]
                   for i in range(size)]

            while p:
                if p & 1:
                    res = mat_mul(res, M)
                M = mat_mul(M, M)
                p >>= 1

            return res

        # Compute T^(n-1)
        P = mat_pow(T, n - 1)

        ans = 0

        for i in range(size):
            for j in range(size):
                ans = (ans + P[i][j] * vec[j]) % MOD

        return ans