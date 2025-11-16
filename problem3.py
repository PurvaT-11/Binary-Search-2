class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l)//2
            if nums[m + 1] > nums[m]: #peak is at the right side, bcz intuitively, numbers are either rising, or will have a drop, either ways, we can find a peak
                l = m + 1
            else:
                r = m # we dont want to loose m, bcz m could be our potential peak, hence not takinf m-1 but m
        return r
