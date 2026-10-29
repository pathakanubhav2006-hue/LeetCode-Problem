class Solution(object):
    def concatWithReverse(self, nums):
        l=nums
        for i in range(len(nums)-1,-1,-1):
            l.append(nums[i])
        return l
        