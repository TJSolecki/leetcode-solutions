class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[(mid + 1) % len(nums)]:
                return nums[(mid + 1) % len(nums)]

            if nums[(mid - 1) % len(nums)] > nums[mid]:
                return nums[mid]

            if (nums[l] <= nums[mid] and nums[r] >= nums[l]) or (
                nums[l] >= nums[r] and nums[mid] <= nums[r]
            ):
                r = mid - 1
            else:
                l = mid + 1

        return nums[0]
