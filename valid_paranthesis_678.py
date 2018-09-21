"""

url : https://leetcode.com/problems/valid-parenthesis-string/description/

 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.

Ex: 
Input: "(*)"
Output: True

Input: "(*))"
Output: True


"""


def valid_paranthesis(s):
	left_index = 0
	right_index = len(s)-1
	while left_index <= right_index :
		if s[left_index] in ('(', '*') and s[right_index] in (')', '*'):
			pass
		elif s[left_index] == s[right_index] == "*":
			pass	
		else:
			return False
		left_index += 1
		right_index -= 1
	return True


print valid_paranthesis("(*)")
print valid_paranthesis("(*))")
print valid_paranthesis("((*")
print valid_paranthesis("(**)")
print valid_paranthesis(")(")
			

			
		
	
