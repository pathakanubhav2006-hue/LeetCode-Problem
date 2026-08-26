class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2
        sum1 = sum2 = 0
        cnt1 = cnt2 = 0
        for i in range(half):
            if num[i] == '?':
                cnt1 += 1
            else:
                sum1 += int(num[i])
        for i in range(half, n):
            if num[i] == '?':
                cnt2 += 1
            else:
                sum2 += int(num[i])
        
        total_q = cnt1 + cnt2
        diff = sum1 - sum2
        
        if total_q % 2 == 1:
            return True
        
        if diff != (cnt2 - cnt1) * 9 // 2:
            return True
        return False
            