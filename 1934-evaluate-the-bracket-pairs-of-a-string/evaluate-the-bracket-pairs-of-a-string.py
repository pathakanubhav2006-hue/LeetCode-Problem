class Solution(object):
    def evaluate(self, s, knowledge):
        mp = {k: v for k, v in knowledge}
        res = []
        key = []
        inside = False

        for ch in s:
            if ch == '(':
                inside = True
                key = []
            elif ch == ')':
                res.append(mp.get("".join(key), "?"))
                inside = False
            elif inside:
                key.append(ch)
            else:
                res.append(ch)

        return "".join(res)