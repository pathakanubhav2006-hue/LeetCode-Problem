class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        charToWord = {}
        wordToChar = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch in charToWord:
                if charToWord[ch] != word:
                    return False
            else:
                if word in wordToChar:
                    return False
                charToWord[ch] = word
                wordToChar[word] = ch

        return True