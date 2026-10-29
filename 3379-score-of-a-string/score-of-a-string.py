class Solution(object):
    def scoreOfString(self, s):
        total=0
        for i in range(1,len(s)):
            total+=abs(ord(s[i-1])-ord(s[i]))
        return total

            
        