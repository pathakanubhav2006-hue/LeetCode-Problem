class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sorted = (nums1+nums2)
        sorted.sort()
        size = len(sorted)
        if size %2 != 0:
            size = (size - 1)/2
            return sorted[size]
        else:
            size = size//2
            return ((float(sorted[size-1])+float(sorted[size]))/2)