class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_table = {}
        for idx, num in enumerate(nums):
            if target-num in num_table:
                return [num_table[target-num], idx]
            num_table[num] = idx
