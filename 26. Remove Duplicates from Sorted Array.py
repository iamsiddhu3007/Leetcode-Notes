class Solution:
  def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    if len(nums) == 0:
      return 0
    elif len(nums) ==1:
      return 1
    left = 1
    right = 1
    while right<len(nums):
      if nums[right] == nums[right-1]:
        nums[left] = nums[right]
        left+=1
      right+=1
    return left
