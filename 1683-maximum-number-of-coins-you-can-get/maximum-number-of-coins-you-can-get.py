class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
    
        total_coins = 0
        n = len(piles) // 3
        for i in range(1, 2 * n, 2):
            total_coins += piles[i]
            
        return total_coins

        