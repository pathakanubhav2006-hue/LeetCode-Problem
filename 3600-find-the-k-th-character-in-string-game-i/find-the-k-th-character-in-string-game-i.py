class Solution(object):
    def kthCharacter(self, k):
        s = 'a'

        while len(s) < k:
            word = ''

            for i in range(len(s)):
                word += chr(ord(s[i]) + 1)

            s += word

        return s[k - 1]