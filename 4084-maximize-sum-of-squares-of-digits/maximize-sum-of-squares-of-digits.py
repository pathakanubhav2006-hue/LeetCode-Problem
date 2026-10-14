class Solution(object):
    def maxSumOfSquares(self, num, sum):
        string = ""
        maximum = sum
        number = 0

    
        if sum > 9 * num:
            return ""

        while num:
            if sum >= 9:
                string += "9"
                sum -= 9
                number += 9
            elif sum > 0:
                string += str(sum)
                number += sum
                sum = 0
            else:
                string += "0"

            num -= 1

        if number == maximum:
            return string
        return ""
