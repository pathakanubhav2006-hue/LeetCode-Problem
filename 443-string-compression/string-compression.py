class Solution(object):
    def compress(self, chars):
        s = ''
        temp = chars[0]
        count = 0

        for i in range(len(chars)):
            if chars[i] == temp:
                count += 1
            else:
                s += temp
                if count > 1:
                    s += str(count)

                temp = chars[i]
                count = 1

        s += temp
        if count > 1:
            s += str(count)

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)