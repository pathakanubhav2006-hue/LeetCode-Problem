class Solution(object):
    def findMissingElements(self, nums):
        l = []
        nums.sort()
        for i in range(1, len(nums)):
            for j in range(nums[i-1] + 1, nums[i]):
                l.append(j)

        return l