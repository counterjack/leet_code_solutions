"""

url : https://leetcode.com/problems/valid-palindrome/description/

Problem : Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Ex:

Input: "A man, a plan, a canal: Panama"
Output: true

Input: "race a car"
Output: false


"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        s = s.strip(" ").upper()
        valid_chars = "".join([string.ascii_uppercase, string.digits])
        s = "".join([i for i in s if i in valid_chars])
        left_index, right_index = 0, len(s)-1
        while left_index <= right_index:
            if s[left_index] != s[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True
            
        
s = "A man, a plan, a canal: Panama"
s = "P"
print isPalindrome(s)
	
	
