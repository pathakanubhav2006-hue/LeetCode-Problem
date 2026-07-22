class Solution(object):
    def modPow(self, a, n):
        a %= 1337
        ans = 1

        while n:
            if n % 2:
                ans = (ans * a) % 1337
            a = (a * a) % 1337
            n //= 2

        return ans

    def superPow(self, a, b):
        ans = 1

        for digit in b:
            ans = self.modPow(ans, 10)
            ans = (ans * self.modPow(a, digit)) % 1337

        return ans