class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = {}
        for i, num in enumerate(nums):
            remainder = target - num;
            if remainder in mem.keys():
                return (mem[remainder], i);
            
            mem[num] = i;

        
