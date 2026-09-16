class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        new_intervals = []

        for i in range(len(intervals)):
            if not new_intervals:
                new_intervals.append(intervals[i])
            
            elif new_intervals[-1][1] >= intervals[i][0]:
                new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
            
            else:
                new_intervals.append(intervals[i])

        return new_intervals