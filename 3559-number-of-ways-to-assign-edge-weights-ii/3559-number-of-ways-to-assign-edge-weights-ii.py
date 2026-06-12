MOD = 10**9 + 7
MAXN = 100005
LOG = 17  # since 2^17 > 1e5

from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges, queries):
        n = len(edges) + 1
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # LCA Preprocessing
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        def dfs(node, par):
            parent[0][node] = par
            for nei in graph[node]:
                if nei == par:
                    continue
                depth[nei] = depth[node] + 1
                dfs(nei, node)
        
        dfs(1, -1)
        
        # Binary lifting
        for i in range(1, LOG):
            for v in range(1, n + 1):
                if parent[i-1][v] != -1:
                    parent[i][v] = parent[i-1][parent[i-1][v]]
        
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            # lift u
            for i in range(LOG):
                if (depth[u] - depth[v]) & (1 << i):
                    u = parent[i][u]
            
            if u == v:
                return u
            
            for i in reversed(range(LOG)):
                if parent[i][u] != parent[i][v]:
                    u = parent[i][u]
                    v = parent[i][v]
            
            return parent[0][u]
        
        # Precompute powers
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        # Answer queries
        res = []
        for u, v in queries:
            if u == v:
                res.append(0)
                continue
            
            w = lca(u, v)
            k = depth[u] + depth[v] - 2 * depth[w]
            
            res.append(pow2[k-1])
        
        return res