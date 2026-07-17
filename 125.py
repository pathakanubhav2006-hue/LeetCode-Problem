class Solution(object):
    def isAlphanumeric(self, ch):
        x = ord(ch)
        if 97 <= x <= 122 or 65 <= x <= 90 or 48 <= x <= 57:
            return True
        return False

    def isPalindrome(self, s):
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i < j:
            if not self.isAlphanumeric(s[i]):
                i += 1
                continue

            if not self.isAlphanumeric(s[j]):
                j -= 1
                continue

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True