
"""
url : https://leetcode.com/problems/valid-palindrome-ii/description/

Description :  Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome. 

Ex: 
Input: "aba"
Output: True

Note:

 # The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


"""

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_index = 0
        right_index = len(s)-1
        deletion_made = 0
        while (left_index <= right_index and deletion_made <= 1):
            if s[left_index] != s[right_index]:
                left_index += 1
                status = self.valid_palindrome_string(s, left_index, right_index)
                if not status:
                    left_index -= 1 # back to original state
                    right_index -= 1
                    status = self.valid_palindrome_string(s, left_index, right_index)
                    if not status:
                        return False                
            else:
                pass
            left_index += 1
            right_index -= 1
        return False or deletion_made <= 1
    
    def valid_palindrome_string(self, s, l, r):
        while (l<=r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
                
                    
print Solution().validPalindrome('abcdbda')	
print Solution().validPalindrome("cupucu")
