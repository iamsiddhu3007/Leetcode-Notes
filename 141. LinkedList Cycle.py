## brute force method
#take a hashset and add the node into it (not the value) keep iterating and when you reach null return false, when you reach to a node that you have in the hashset, return true
# can you floyd tortoise hare algorithm-> take 2 pointers slow, fast: slow increments by 1, fast increments by 2, when the slow pointer = fast pointer return true, if fast reaches null, or slow reaches null return true

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
