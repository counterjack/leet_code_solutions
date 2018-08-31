"""

link : https://leetcode.com/problems/add-two-numbers/description/

Example : 

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        final_list = []        
        remainder = 0
        while l1 or l2:                
            sum_ = 0
            try:
                sum_ += l1.val
                l1 = l1.next
            except:
                pass
            try:
                sum_ += l2.val
                l2 = l2.next
            except:
                pass
            sum_ += remainder          
        
            final_list.append(sum_%10)
            remainder = sum_ //10 
            if not l1 and not l2 and remainder!=0:
                final_list.append(remainder)
            
        
        return final_list
            
            
