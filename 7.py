class Solution(object):
    def reverse(self, x):
        t = str(x)

        if t[0] == '-':
            t = int('-' + t[1:][::-1])
        else:
            t = int(t[::-1])

        if -(2**31) <= t <= (2**31 - 1):
            return t
        return 0