class Solution(object):
    def pickGifts(self, gifts, k):
        gifts.sort()
        n = len(gifts)
        while k:
            gifts[n-1] = int(gifts[n-1] ** 0.5)
            gifts.sort()  # re-sort so new max is at the end again
            k -= 1
            
        return int(sum(gifts))