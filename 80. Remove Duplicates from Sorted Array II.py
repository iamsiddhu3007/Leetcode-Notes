class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) ==1:
            return 1
        elif len(nums) == 2:
            return 2
        
        left = 2
        right = 2
        while right < len(nums):
            if nums[right] != nums[left -2]:
                nums[left] = nums[right]
                left+=1
            right+=1
        return left
