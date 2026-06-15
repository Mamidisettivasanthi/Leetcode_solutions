class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for i in range(len(accounts)):
            total = sum(accounts[i])
            if total > maximum:
                maximum = total
        return maximum


        