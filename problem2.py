class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l , r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2

            if nums[m] > nums[r]: #the number lies in the right half (since rotation wraps around)
                l = m + 1
            else: #the number lies in the left side and m can still be a possible asnwer, hence we dont skip over m
                r = m
        return nums[l]