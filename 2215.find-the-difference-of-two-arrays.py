class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res = [set(), set()]
        for num in nums1:
            if num not in nums2:
                res[0].add(num)
        for num in nums2:
            if num not in nums1:
                res[1].add(num)

        return list(map(list, res))
