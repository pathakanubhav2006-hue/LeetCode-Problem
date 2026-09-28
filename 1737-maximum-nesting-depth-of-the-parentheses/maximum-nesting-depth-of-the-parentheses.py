class Solution(object):
    def maxDepth(self, s):
        max_par=0
        count=0
        for i in range(len(s)):
            if s[i] in "(":
                count+=1
            elif s[i] in ")":
                count-=1
            if count > max_par:
                max_par=count
        return max_par
        