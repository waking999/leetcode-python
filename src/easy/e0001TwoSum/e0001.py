class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        length = len(nums)
        for i in range(length):
            a = nums[i]
            b = d.get(target - a)
            if b is None:
                d[a] = i
            else:
                return [b, i]
