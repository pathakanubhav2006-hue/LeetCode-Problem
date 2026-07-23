class Solution(object):
    def searchRange(self, nums, target):
        arr = []

        for i in range(len(nums)):
            if nums[i] == target:
                if len(arr) == 0:
                    arr.append(i)
                if len(arr) == 1:
                    arr.append(i)
                else:
                    arr[1] = i

        if len(arr) == 0:
            return [-1, -1]
        if len(arr) == 1:
            return [arr[0], arr[0]]

        return arr