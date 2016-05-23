#Count letters in a name


def count(name):
	name_dict = {}
	for i in str.lower(name):
		if i not in name_dict:
			name_dict[i] = 1
		else: 
			name_dict[i] += 1
	return name_dict

print(count("Elizabeth"))