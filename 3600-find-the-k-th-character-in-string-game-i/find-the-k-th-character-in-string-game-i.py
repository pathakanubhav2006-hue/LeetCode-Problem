class Solution(object):
    def kthCharacter(self, k):
        def solve(s):
            if len(s) >= k:
                return s[k - 1]

            word = ''
            for i in range(len(s)):
                word += chr(ord(s[i]) + 1)

            s += word

            return solve(s)

        return solve('a')