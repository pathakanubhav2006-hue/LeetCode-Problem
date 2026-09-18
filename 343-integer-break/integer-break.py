class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        # n is now 2, 3, or 4 (n <= 4 handles the 2x2 vs 1x3 edge case)
        product *= n
        return product