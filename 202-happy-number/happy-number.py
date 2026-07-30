class Solution(object):
    def isHappy(self, n):
        def getSum(num):
            s = 0
            while num > 0:
                digit = num % 10
                s += digit * digit
                num //= 10
            return s

        slow = n
        fast = getSum(n)

        while fast != 1 and slow != fast:
            slow = getSum(slow)
            fast = getSum(getSum(fast))

        return fast == 1