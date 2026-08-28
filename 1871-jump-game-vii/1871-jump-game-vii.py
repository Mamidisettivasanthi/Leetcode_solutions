class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] != '0':
            return False

        reachable = [False] * n
        reachable[0] = True

        count = 0

        for i in range(1, n):
            # Add positions that have now entered the jump range
            if i - minJump >= 0 and reachable[i - minJump]:
                count += 1

            # Remove positions that are now outside the jump range
            if i - maxJump - 1 >= 0 and reachable[i - maxJump - 1]:
                count -= 1

            # Current position is reachable if there is at least
            # one reachable position in the valid range
            if s[i] == '0' and count > 0:
                reachable[i] = True

        return reachable[n - 1]