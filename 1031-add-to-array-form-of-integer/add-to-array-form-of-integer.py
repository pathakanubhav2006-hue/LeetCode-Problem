class Solution(object):
    def addToArrayForm(self, num, k):
        s = ""
        for i in range(len(num)):
            s += str(num[i])

        n = int(s) + k

        ans = []
        while n > 0:
            ans.append(n % 10)
            n //= 10

        if not ans:
            return [0]

        return ans[::-1]