class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0 #check the occurence of 9 as last element if all the elements are 9 then it will be converted to 0 and then we will concatenate the array by adding [1]

        return [1] + digits