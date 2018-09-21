#/bin/python
"""
Prob : 
Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".


"""


class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
	        :rtype: str
		"""
		# clean path ignores duplicate '/' and '.'
		clean_path = "/"+ "/".join(filter(lambda item:item not in ('', '.'), path.split("/"))) + "/"		
		cleaned_path_list = clean_path.split("/")
		idx , stack = 0, []	
		cleaned_path_list = [i for i in cleaned_path_list if i != '' ]
		while idx < len(cleaned_path_list):
			if cleaned_path_list[idx] == "..":
				try:
					popped_item = stack.pop()
					if popped_item == "":	
						stack.append("")
	
				except Exception as e:	
					pass
			else:
				stack.append(cleaned_path_list[idx])
			idx +=1
		res = "/" + "/".join(stack)
		return res
