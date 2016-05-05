"""Create a program that helps calculate the bill. 
It will be able to do three things. 
Calculate Tip given the bill amount and tip percentage
Calculate Total Bill given the tip amount and bill amount
Split a bill given the bill amount and the number of people 
to split the amount for.
"""
bill_amount = 100
tip_pct = .15
number_of_people = 5


def calc_tip():
	return bill_amount * tip_pct

def total_bill():
	return calc_tip() + bill_amount

def split_bill():
	return total_bill()/number_of_people

print split_bill()
