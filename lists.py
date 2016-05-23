days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def prompt_user():
	return input("What day of the week is it? ")

def display_tomorrow(today):
	if today in days_of_week:	
		tomorrow = days_of_week.index(today) + 1
		if tomorrow == 7: 
			print (days_of_week[0])
		elif tomorrow < 7:
			print(days_of_week[tomorrow])
	else: 
		print("You didn't enter a real day")

def main():
	display_tomorrow(prompt_user())

if __name__ == '__main__':
	main()

# Alternative display_tomorrow function

def display_tomorrow2(today):
	tomorrow = (days_of_week.index(today) + 1) % len(days_of_week)
	print ('Tomorrow is', days_of_week[tomorrow])