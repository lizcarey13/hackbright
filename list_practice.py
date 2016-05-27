def pair(x, y):
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def count(s, value):
	index, total = 0, 0
	while index < len(s):
		if s[index] == value:
			total += 1
		index += 1
	return total

#improve count with a for statement

def count2(s, value):
	total = 0
	for item in s: 
		if item == value: 
			total += 1

	return total

# Sequence unpacking

pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]

same_count = 0

for x, y in pairs:
	if x == y: 
		same_count += 1

#print(same_count)

def divisors(n):
	"""
	>>> divisors(6)
	[1, 2, 3]
	>>>
	"""
	return [x for x in range(1, n) if n % x == 0]

def right_binarize(tree):
	"""Construct a right-branching binary tree."""
	if is_leaf(tree):
		return tree
	if len(tree) > 2:
		tree = [tree[0], tree[1:]]
	return [right_binarize(b) for b in tree]

def tree(root, branches = []):
	for branch in branches: 
		assert is_tree(branch), 'branches must be trees'
	return [root] + list(branches)

def root(tree):
	return tree[0]

def branches(tree):
	return tree[1: ]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
		return True

def is_leaf(tree): 
	return not branches(tree)

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])

print(t)






