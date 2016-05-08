


choice = int(raw_input("What would you like to do? Enter 1 to calculate the tip, and 2 to find the cost per person"))
print choice

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
