class Solution(object):

    def arrangeCoins(self, n):
        count = 0
        i = 0
        j = 1

        while i < n:
            i = i + j
            j = j + 1
            count += 1

        if i == n:
            return count
        else:
            return count - 1