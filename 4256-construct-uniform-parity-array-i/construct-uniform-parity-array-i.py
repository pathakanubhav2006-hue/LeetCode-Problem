class Solution(object):
    def uniformArray(self, nums1):
        odd = 0
        even = 0

        for x in nums1:
            if x % 2:
                odd += 1
            else:
                even += 1
        if odd >= 2 and even >= 2:
            return True
        if odd > 0 and even > 0:
            return True

        if odd == len(nums1) or even == len(nums1):
            return True

        return False