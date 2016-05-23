# Given a food tuple, where all the odd positions are the names of the food, 
# and all the even positions are the corresponding prices, i.e.:
food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)


# Write a function to convert the food tuple into a food dictionary where we 
# can use food name as key to access its price, i.e.:
# > print food_dictionary['sushi']
# > 7.50

def convert_tuple_to_dict(tuple_name):
	food_dict = {}
	count = 0
	for i in tuple_name: 
		if count % 2 == 0: 
			food_dict[i] = tuple_name[count + 1]
		count += 1
	return food_dict

	

food_dictionary = convert_tuple_to_dict(food_price_tuple)


print (food_dictionary)
print (food_dictionary['sushi'])

def convert_tuple_to_dict2(tuple_name): 
	count = 0
 	food_dict = {x:tuple_name(count+1) for x in tuple_name}
