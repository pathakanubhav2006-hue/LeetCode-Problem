class Solution(object):
    def rotate(self, matrix):
        for row in range(len(matrix)):
            for column in range(row+1,len(matrix[row])):
                matrix[row][column],matrix[column][row]=matrix[column][row],matrix[row][column]
        
        for row in range(len(matrix)):
            matrix[row].reverse()


        