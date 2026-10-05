class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        counter=0
        digit=str(digit)
        for i in range(len(nums)):
            string=str(nums[i])
            counter+=string.count(digit)
        return counter
        