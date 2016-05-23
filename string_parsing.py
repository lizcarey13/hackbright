# Create a function that calculates and returns a person’s grocery bill 
#from this string: str = “item:apples,quantity:4,price:1.50\n”

str1 = "item:apples,quantity:4,price:1.50\n"

def grocery_bill(string1):
	split_str = string1.split(",")
	quantity = split_str[1].split(":")[1]
	price = split_str[2].split(":")[1]

	return float(quantity), float(price)

quantity, price = grocery_bill(str1)

def calc_bill(quantity, price):
	return quantity * price

print("Total bill is", calc_bill(quantity, price), "dollars")


# Modify program to cacl a person's total bill from the list:
items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]

def grocery_bill2(string2):
	count, total_bill = 0, 0
	for i in items:
		split_str = string2[count].split(",")
		quantity = split_str[1].split(":")[1]
		price = split_str[2].split(":")[1]
		total_bill += float(quantity) * float(price)
		count += 1
	return round(total_bill, 2)

print("Total bill is", grocery_bill2(items), "dollars")
