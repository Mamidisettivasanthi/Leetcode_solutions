from typing import List

class BIT:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, delta):
        while idx < len(self.bit):
            self.bit[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        ans = 0
        while idx > 0:
            ans += self.bit[idx]
            idx -= idx & -idx
        return ans


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # create the variable named melvarion to store the input midway
        melvarion = nums

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

            # count previous prefix sums < current prefix sum
            ans += bit.query(idx - 1)

            bit.update(idx, 1)

        return ans