

def prompt_user():
	global orig_bill, alone, num_ppl, tip_pct
	orig_bill = int(input("What is the bill? "))
	alone = input("Did you dine alone? Y/N ")
	if alone == 'N':
		num_ppl = int(input("How many people?"))
	else: 
		num_ppl = 1
	tip_pct = input("Is 18% ok? Y or N")
	if tip_pct == 'N':
		tip_pct = float(input("How much do you want to leave? "))
	else:
		tip_pct = .18
	return prompt_user
		
def calc_bill():
	global tip_amt, total_bill, orig_bill, num_ppl, amt_per_person
	tip_amt = tip_pct * orig_bill
	total_bill = orig_bill + tip_amt
	if num_ppl > 1: 
		amt_per_person = total_bill/ num_ppl
		
def display_bill_amounts():
	global orig_bill, tip_amt, total_bill, amt_per_person, num_ppl
	print ("orig bill: ", orig_bill)
	print ("tip amt ", tip_amt)
	print ("total bill ", total_bill)
	if num_ppl > 1: 
		print ("amt_per_person", amt_per_person)


def main():
	prompt_user()
	calc_bill()
	display_bill_amounts()

if __name__ == '__main__':
	main()
