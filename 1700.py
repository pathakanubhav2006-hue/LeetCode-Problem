class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        Count how many students won't be able to eat sandwiches.
        Uses a frequency map to track students by preference (0 or 1).
        """
        d = {0: 0, 1: 0}
        for i in students:
            d[i] += 1
        
        for i in range(len(sandwiches)):
            if d[sandwiches[i]] == 0:
                return len(sandwiches) - i
            d[sandwiches[i]] -= 1
        
        return 0