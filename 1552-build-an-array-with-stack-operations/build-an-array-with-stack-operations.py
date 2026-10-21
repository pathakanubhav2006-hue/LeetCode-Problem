class Solution:
    def buildArray(self, target, n):
        k = 0
        s = []
        
        for i in range(1, n + 1):
            if k >= len(target):
                break
                
            s.append("Push")
            if target[k] == i:
                k += 1
            else:
                s.append("Pop")
                
        return s
