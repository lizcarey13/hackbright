food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)

def convert_tuple_to_dict(tuple_name):
	#create an empty dictionary
	food_dict = {}
	#create counter to count index
	index = 0
	#loop through each item
	for i in tuple_name: 
		#If we have even index
		if index % 2 == 0:
			#add that as a key for the dictionary
			# the next item is the value
			food_dict[tuple_name[index]] = tuple_name[index + 1]

		#incremnet index
		index += 1
	return food_dict

print(convert_tuple_to_dict(food_price_tuple))

##String Parsing

str1 = "item:apples,quantity:4,price:1.50\n"
def total_bill(groceries):

	str_list = groceries.split(",")
	quantity_list = str_list[1].split(":")
	quantity = int(quantity_list[1])

	price_list = str_list[2].split(":")

	price = float(price_list[1])

	total_bill = quantity * price


	return total_bill

print(total_bill(str1))


			