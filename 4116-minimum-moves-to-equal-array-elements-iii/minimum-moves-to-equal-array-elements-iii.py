class Solution(object):
    def minMoves(self, nums):
        maximum=max(nums)
        mintotal=0
        for i in range(len(nums)):
            if nums[i]!=maximum:
                mintotal+=(maximum-nums[i])
        return mintotal
        