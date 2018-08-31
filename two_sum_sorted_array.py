"""

link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Desc: 

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

"""


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = left_index = 0
        right_index = len(numbers) - 1
        while ( left_index <= right_index or index<len(numbers)):
            left_ele = numbers[left_index]
            right_ele = numbers[right_index]
	    sum_ = left_ele + right_ele
           
            if sum_ < target:
                left_index += 1
            elif sum_ > target:
                right_index -= 1
            else:
                return (left_index+1, right_index+1)
            
            index += 1
            
arr = [2, 7, 11, 15]
a = Solution()
print a.twoSum(arr, 9)
