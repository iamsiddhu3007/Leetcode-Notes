'''
if i want to merge to sorted arrays, I can start from the end. It means that I can start by taking the largest of the two arrays and placing at the last element in the nums1 array
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        last = m+n -1
        # merge in reverse order
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last -= 1
        #after filling if n has more number of elements or first element of n is greater than the first element of m then we need to fill up all the remaining elements in n at the start of m
        while n>0:
            nums1[last] = nums2[n-1]
            n-=1
            last-=1
