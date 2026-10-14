class Solution(object):
    def numberOfBeams(self, bank):
        prev = 0
        beams = 0

        for row in bank:
            count = row.count('1')

            if count > 0:
                beams += prev * count
                prev = count

        return beams
