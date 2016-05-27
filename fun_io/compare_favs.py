my_file = open("liz_fav_foods.txt")
liz_favs = my_file.readlines()
my_file.close()


my_file2 = open("dan_fav_foods.txt")
dan_favs = my_file2.readlines()
my_file2.close()

# with open("liz_fav_foods.txt") as my_file2:
# 	my_file2 = my_file.read()


def compare_favs2(list1, list2):
	same_items = []
	diff_items = []
	for item in list1: 
		for item2 in list2:
			if item in item2:
				print("We both love", item)
				if item not in same_items:
					same_items.append(item)
			else:
				if item not in diff_items:
					diff_items.append(item)
	for item in same_items:
		print("You both love", item)
	print("Only one of you loves", diff_items)

compare_favs2(liz_favs, dan_favs)
