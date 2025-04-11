class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square_sum(num):
            num = str(num)
            sum =0
            for i in num:
                sum += int(i)**2
            return sum
        my_set = set()
        i = square_sum(n)
        while i != 1:
            if i not in my_set:
                my_set.add(i)
                i = square_sum(i)
            if i in my_set:
                return False
        return True

## better approach is linkedlist cycle
