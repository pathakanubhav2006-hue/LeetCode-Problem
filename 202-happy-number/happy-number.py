class Solution(object):
    def isHappy(self, n):
        seen = set()

        def solve(num):
            if num == 1:
                return True
            if num in seen:
                return False

            seen.add(num)

            s = 0
            while num > 0:
                digit = num % 10
                s += digit * digit
                num //= 10

            return solve(s)

        return solve(n)