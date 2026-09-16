class Solution(object):
    def rotate(self, matrix):
        #transpose of matrix
        for row in range(len(matrix)):
            for column in range(row+1,len(matrix[row])):
                matrix[row][column],matrix[column][row]=matrix[column][row],matrix[row][column]

        
        #reversing all the rows
        #for row in range(len(matrix)):
        #    matrix[row].reverse
            
        for row in range(len(matrix)):
            left = 0
            right = len(matrix)-1

            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1


        