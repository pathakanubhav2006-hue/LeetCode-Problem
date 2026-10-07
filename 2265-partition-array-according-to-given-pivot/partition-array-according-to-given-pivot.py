class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less_pivot, more_pivot = [], []
        count_pivot = 0

        for i, num in enumerate(nums):
            if num > pivot:
                more_pivot.append(num)
            elif num < pivot:
                less_pivot.append(num)
            else:
                count_pivot += 1

        return less_pivot + [pivot] * count_pivot + more_pivot