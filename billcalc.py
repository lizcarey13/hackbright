def main():
	def prompt_user():
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
	
	def calc_bill():
		tip_amt = tip_pct * orig_bill
		total_bill = orig_bill + tip_amt
		amt_per_person = total_bill/ num_ppl
	
	def display_bill_amounts():
		print ("orig bill: ", orig_bill)
		print ("tip amt ", tip_amt)
		print ("total bill ", total_bill)
		print ("amt_per_person", amt_per_person)

	return prompt_user, calc_bill, display_bill_amounts
	
main()

