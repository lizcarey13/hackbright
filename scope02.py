


choice = int(raw_input("What would you like to do? Enter 1 to calculate the tip, and 2 to find the cost per person"))

bill_amount = 100
tip_pct = .15
number_of_people = 5


def calc_tip():
	return bill_amount * tip_pct

def total_bill():
	return calc_tip() + bill_amount

def split_bill():
	return total_bill()/number_of_people

if choice ==1: 
	print "Your tip is", calc_tip(), "with a bill total of", total_bill()
	bill_split = int(raw_input("Would you like the bill split?"))
	if bill_split == 1:
		num_ppl = int(raw_input("How many ways should I split the bill?"))
		return total_bill()/num_ppl
elif choice == 2:
	print "The cost per person is", split_bill()
