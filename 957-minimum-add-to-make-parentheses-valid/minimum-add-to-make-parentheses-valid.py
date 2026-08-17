class Solution(object):
    def minAddToMakeValid(self, s):
        count = 0
        add = 0

        for i in range(len(s)):
            if s[i] == "(":
                count += 1

            if s[i] == ")":
                if count > 0:
                    count -= 1
                else:
                    add += 1

        return count + add