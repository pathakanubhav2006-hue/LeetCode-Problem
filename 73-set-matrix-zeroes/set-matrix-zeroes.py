class Solution(object):
    def setZeroes(self, matrix):
        rows = set()
        columns = set()

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    rows.add(row)
                    columns.add(column)

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if row in rows or column in columns:
                    matrix[row][column] = 0

        return matrix