# Create a dictionary called vocabulary_words that contains 4 
# vocabulary words

vocabulary_words = {"one": 1, "Two": 2, "Three": 3, "Four": 4}

#Write a function that counts how many times each letter appears 
#in your full name. Return a dictionary that looks like this: {‘a’:2, ‘c’:1, ‘w’:1} 
#(Hint: Case matters!)

name_dict = {}
def count(name):
	for i in str.lower(name):	
		if i not in name_dict:
			name_dict[i] = 1
		else: 
			name_dict[i] += 1
	return name_dict

# Given a dictionary of items and their prices, write a program 
# that returns the most expensive item. Hint: Look at the Dictionary 
# lecture to figure out how to iterate over a dictionary!
# e.g. prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3 }
#Your program should return “banana”

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

highest_value, highest_key = 0, ""
for key, value in prices.items():
	if value > highest_value:
		highest_key, highest_value = key, value
print (highest_key, highest_value)

### Alternative:

# prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# highest_key_val_pair = list(prices.values())[0]
# for key, value in range(1, len(prices):
# 	if value > highest_value:
# 		highest_key, highest_value = key, value
# print (highest_key, highest_value)

# prices.items()[1:]

###Alternative 2:

highest_value = list(prices.items())[0][1]
highest_key = list(prices.items())[0][0]
index = 1
while index < len(prices):
 	if list(prices.items())[index][1] > highest_value:
 		highest_value = list(prices.items())[index][1]
 		highest_key = list(prices.items())[index][0]
 	index += 1 
print(highest_key, highest_value)


	
employee = {}
employee = {"name": "Rachel", "age": 27, "height": float(input("What is you height? ")) }
employee["age"] = 28

#Check if a key exists, if so access the value
if "name" in employee:
	print ("name", employee["name"])
else: print ("Key: name exists")

#Check if a key exists, if so access the value
if 26 in employee:
    print ("Key:", 26, employee[26])
else: print ("Key: 26 does not exist.")

for key, value in employee.items():
	if key == "name":
		print(key, value)
	if value == 26:
		print(key, value)
	else:
		print(26)


