class Solution(object):
    def maximumWealth(self, accounts):
        n = len(accounts)
        max1 = 0

        for i in range(n):
            sum1 = 0
            for j in range(len(accounts[i])):
                sum1 += accounts[i][j]
            if max1 < sum1:
                max1 = sum1

        return max1