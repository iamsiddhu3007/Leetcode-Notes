class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        #reverse the entire array
        left = 0
        right = len(nums) - 1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        #reverse the first part of the array
        left = 0
        right = k-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        #reverse the second part of the array
        left = k
        right = len(nums) - 1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        
