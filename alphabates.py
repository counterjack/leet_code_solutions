# bin/python
"""
A-> 1
B-> 2
c-> 3
D-> 4
...
Z -> 26

ex : n=123,
combinations will be  : [(1,2,3), (12,3), (1, 23)] => [ABC, LC, AW]

"""

def get_all_combinations(n):
	alphabets_mapping = {idx+1:item  for idx, item in enumerate(string.ascii_uppercase)}
	arr = []
	combinations = []
	while n:
		arr.insert(0, n%10)
		n = n/10
	
	# one basic combination will be numbers individually
	combinations.append("".join([alphabets_mapping[i] for i in arr])]
	for idx, i in enumerate(arr):
		
		pass
