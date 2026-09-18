class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        if n < 1:
            return False
        power = 1
        x = n 
        while power < n:
            power *= 3
        return power == n