from typing import List
from collections import deque

class Solution:
    def remainingMethods(
        self,
        n: int,
        k: int,
        invocations: List[List[int]]
    ) -> List[int]:

        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        # Find all methods suspicious because they are
        # reachable from method k.
        suspicious = [False] * n
        suspicious[k] = True

        q = deque([k])

        while q:
            u = q.popleft()

            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        # If a non-suspicious method invokes a suspicious
        # method, we cannot remove the suspicious methods.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Otherwise remove all suspicious methods.
        return [i for i in range(n) if not suspicious[i]]