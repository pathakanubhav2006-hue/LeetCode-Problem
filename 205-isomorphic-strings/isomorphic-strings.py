class Solution(object):
    def isIsomorphic(self, s, t):
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            if s[i] in mapST:
                if mapST[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapTS:
                    return False
                mapST[s[i]] = t[i]
                mapTS[t[i]] = s[i]

        return True