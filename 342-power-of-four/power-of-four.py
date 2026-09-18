class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        if n < 1:
            return False
        power = 1
        x = n 
        while power < n:
            power *= 4
        return power == n