class Solution(object):
    def targetIndices(self, nums, target):
        new_list=list()
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                new_list.append(i)
        return new_list
        