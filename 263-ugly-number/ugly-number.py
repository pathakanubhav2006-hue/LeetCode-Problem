class Solution(object):
    def isUgly(self, n):
        def check(n):
            if n <= 0:
                return False
            if n == 1:
                return True

            if n % 2 == 0:
                return check(n // 2)

            if n % 3 == 0:
                return check(n // 3)

            if n % 5 == 0:
                return check(n // 5)

            return False

        return check(n)