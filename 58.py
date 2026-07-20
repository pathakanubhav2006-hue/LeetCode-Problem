class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split() 
        if not word:
            return 0
            
        return len(word[-1])

        