class Solution(object):
    def minOperations(self, nums, k):
        sum_number=0
        for i in range(len(nums)):
            sum_number+=nums[i]
        
        return sum_number%k