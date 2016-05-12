"""Create a list called fruits that contains “apples”, “oranges”, and “bananas”
Using a for ­loop, and not using the range function, go through the list, 
and print out each fruit.
"""


fruits = ["apples", "oranges", "bananas"]

for item in fruits:
	print (item, end=" ")

#Using a for loop, and using the range function, go through the list and print 
#out each fruit. Hint: You should use the len() function.

for item in range(len(fruits)):
	print (fruits[item], end=" ")

"""Create a function called sum_nums that takes in a number called num. 
sum_nums should add up all of the numbers from 0 until (but not including) 
num. sum_nums should return this sum.

>>>print(sum_nums(3))
3
"""

def sum_nums(num):
	count = 0
	for i in range(num):
		count += i 
	return count

#Modify sum_nums to add up all the numbers from 0 to num, including num.

def sum_nums(num):
	count = 0
	for i in range(num+1):
		count += i 
	return count

def sum_nums2(num):
	count = 0
	if num < 0:
		for i in range(0, num-1, -1):
			count += i	
	else: 
		for i in range(num+1):
			count += i
	return count

"""Write a function called fizz_buzz that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the 
number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five 
print “FizzBuzz”."""

def fizz_buzz():
	for i in range(101):
		if i % 15 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0: 
			print("Buzz")
		else:
			print(i)