class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        string = ""
        for ch in s:
            if ch.isalpha():
                string += ch
            elif ch == "(":
                stack.append(string)   # save text before this "("
                string = ""
            elif ch == ")":
                string = stack.pop() + string[::-1]  # reverse current, attach to saved prefix
        return string