class Solution:
    def shortestToChar(self, s: str, c: str):
        arr = []
        positions = []
        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)
        for i in range(len(s)):
            min_dist = float('inf')
            for pos in positions:
                min_dist = min(min_dist, abs(i - pos))
            arr.append(min_dist)
        return arr