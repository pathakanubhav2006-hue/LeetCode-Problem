class Solution(object):
    def maxProduct(self, nums):
        maximum = nums[0]
        minimum = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maximum, minimum = minimum, maximum

            maximum = max(nums[i], maximum * nums[i])
            minimum = min(nums[i], minimum * nums[i])

            answer = max(answer, maximum)

        return answer