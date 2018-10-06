"""
Url : https://leetcode.com/problems/integer-to-roman/description/

Desc : 

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

Example 2:

Input: 4
Output: "IV"

Example 3:

Input: 9
Output: "IX"

Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Logic:

LR Rule: 

roman_units = [1, 5, 10, 50, 100, 500, 1000]

eg: num = 7, left_close = 5, right_close = 10, 
	but num/right_close > 0.8 is false then right else left
	so close_unit to 7 will be 5.
    num = 90, left_close = 50, right_close = 100
	but num/right_close > 0.8 is true
	so close unit to 90 will be 100
"""

class Solution:
    roman_units = [1, 5, 10, 50, 100, 500, 1000]
    roman_mapper = {
	1: 'I',
	5 : 'V',
	10 : 'X',
	50 : 'L',
	100: 'C',
	500: 'D',
	1000: 'M'
	}
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
       	place = 1
	items_with_place = []
	num_copy  = num
	# list for unit places
	while num_copy:
		digit = num_copy%10
		items_with_place.insert(0, place*digit)
		num_copy = num_copy >> 1
		place = place*10
	print items_with_place
	
	final_res = []
	for item in items_with_place:
		if item > 1000: # eg : 3000
			final_res.append(self.roman_mapper[1000]*(item/1000))
		else:
			flag, close_roman = self.get_closer_roman(item)
			if flag:
				final_res.append(self.roman_mapper[close_roman])
				continue
			
		

    def get_closer_roman(num):
	"""
	i/p: num
	o/p: closest roman unit based on the LR Logic
	
	
	"""
	left = right = 0
	for idx, item in  enumerate(self.roman_units):
		if item < num < self.roman_units[idx+1]  :
			left, right = item, self.roman_units[idx+1]
		else:
			return True, self.roman_mapper[num]
	
	return  False, right if num*10/right >= 9 else left
	

		
		
	
		
		 
