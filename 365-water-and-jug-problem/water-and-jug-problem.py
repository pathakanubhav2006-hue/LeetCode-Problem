class Solution(object):
    def canMeasureWater(self, x, y, target):
        if target>(x+y):
            return False
        while y != 0:
            x, y = y, x % y
        target1=x
        if target%target1==0:
            return True
        else:
            return False
        