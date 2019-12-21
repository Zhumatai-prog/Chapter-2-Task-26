list_of_numbers = input("Enter a list of numbers: ")
list_of_numbers = list_of_numbers.split(",")
list_ = list(list_of_numbers)

print(list_)
odds = 0
evens = 0
for i in list_:
	if int(i) % 2 == 0:
		evens = evens + 1
	else:
		odds = odds + 1

print(f"{evens} evens and {odds} odds")