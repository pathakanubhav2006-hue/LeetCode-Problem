class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0]
        for d in days:
            prefix.append(prefix[-1] + d)

        def to_day(s):
            m = int(s[:2])
            d = int(s[3:])
            return prefix[m - 1] + d

        start = max(to_day(arriveAlice), to_day(arriveBob))
        end = min(to_day(leaveAlice), to_day(leaveBob))
        return max(0, end - start + 1)