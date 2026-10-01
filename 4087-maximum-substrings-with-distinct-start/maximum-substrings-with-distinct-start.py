class Solution(object):
    def maxDistinct(self, s):
        L=[]
        for i in range(len(s)):
            if s[i] not in L:
                L.append(s[i])
            
        return len(L)
        