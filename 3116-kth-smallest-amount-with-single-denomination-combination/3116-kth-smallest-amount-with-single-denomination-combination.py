from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Precompute the LCM for all possible subsets of coins
        # to efficiently apply the Principle of Inclusion-Exclusion (PIE)
        n = len(coins)
        lcm_subsets = []
        
        # Generate subsets from size 1 to n
        for r in range(1, n + 1):
            for subset in combinations(coins, r):
                # Calculate LCM for the current subset
                current_lcm = subset[0]
                for coin in subset[1:]:
                    current_lcm = (current_lcm * coin) // gcd(current_lcm, coin)
                
                # Store the LCM along with the subset size (to know sign in PIE)
                lcm_subsets.append((current_lcm, r))
        
        # Helper function to count how many valid amounts are <= target
        def count_amounts_le(target: int) -> int:
            total_count = 0
            for lcm_val, size in lcm_subsets:
                # PIE: Add odd-sized subsets, subtract even-sized subsets
                if size % 2 == 1:
                    total_count += target // lcm_val
                else:
                    total_count -= target // lcm_val
            return total_count

        # Binary search range for the answer
        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_amounts_le(mid) >= k:
                ans = mid       # mid could be our answer, but look for smaller
                high = mid - 1
            else:
                low = mid + 1   # Not enough amounts, look higher
                
        return ans
