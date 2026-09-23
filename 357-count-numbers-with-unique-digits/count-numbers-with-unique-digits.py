class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 10
        else:
            perm = 9
            count = 0
            for i in range(1, n):
                k = 10
                perm = perm * (k - i)
                count = count + perm
            return count + 10