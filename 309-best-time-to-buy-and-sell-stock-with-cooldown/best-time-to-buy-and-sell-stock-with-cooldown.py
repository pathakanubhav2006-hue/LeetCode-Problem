class Solution(object):
    def maxProfit(self, prices):
        memo = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0

            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            if canBuy:
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)
                ans = max(buy, skip)
            else:
                sell = prices[i] + dfs(i + 2, True)   # cooldown
                hold = dfs(i + 1, False)
                ans = max(sell, hold)

            memo[(i, canBuy)] = ans
            return ans

        return dfs(0, True)