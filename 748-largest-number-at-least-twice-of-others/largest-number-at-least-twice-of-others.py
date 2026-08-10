class Solution(object):
    def dominantIndex(self, nums):
        max1 = -1
        ans = 0

        for i in range(len(nums)):
            if nums[i] > max1:
                max1 = nums[i]
                ans = i

        for i in nums:
            if i != max1 and i * 2 > max1:
                return -1

        return ans