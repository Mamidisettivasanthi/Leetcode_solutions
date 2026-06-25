from typing import List

class BIT:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, idx, val):
        while idx < len(self.tree):
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & -idx
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pref = [0]
        cur = 0

        for x in nums:
            if x == target:
                cur += 1
            else:
                cur -= 1
            pref.append(cur)

        vals = sorted(set(pref))
        comp = {v: i + 1 for i, v in enumerate(vals)}

        bit = BIT(len(vals))

        ans = 0

        for p in pref:
            idx = comp[p]

            # count previous prefix sums strictly smaller than p
            ans += bit.query(idx - 1)

            bit.update(idx, 1)

        return ans