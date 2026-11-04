class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums) // 2]
        total_moves = 0
        for num in nums:
            total_moves += abs(num - median)
            
        return total_moves             
        

        