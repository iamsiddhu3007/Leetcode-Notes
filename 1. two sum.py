class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        my_dict[nums[0]] = 0
        for i in range(1, len(nums)):
            if target - nums[i] in my_dict:
                return [my_dict[target-nums[i]], i]
            my_dict[nums[i]] = i
