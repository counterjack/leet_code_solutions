"""
 

link : https://leetcode.com/problems/palindrome-number/description/


Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        left_index = 0
        right_index  = len(x)-1
        
        while left_index <= right_index:
            if x[left_index] != x[right_index]:
                return False
	    left_index += 1
	    right_index -= 1
        
        return True


st = "1213"
a = Solution().isPalindrome(st)
print a
        
