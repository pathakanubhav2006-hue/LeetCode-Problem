class Solution(object):
    def reverseWords(self, s):
        s=(s.strip()).split()
        s.reverse()

        return " ".join(s)


        