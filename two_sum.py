#/bin/python
"""

Link : https://leetcode.com/problems/two-sum/description/

Desc:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

# array may or may not be sorted
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for idx, i in enumerate(nums):
            dic[i] = idx
     
        indexes = []
        for idx, item in enumerate(nums):
            required_sum  = target - item
            
            try:
                another_idx = dic[required_sum]
		if another_idx == idx:
		    continue
                indexes = (idx, another_idx)
                break
            except:
                pass
        return indexes


arr = [3, 2, 4]

a = Solution()
print a.twoSum(arr, 6)
