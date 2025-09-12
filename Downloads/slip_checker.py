#greet user
#ask user to put their betting numbers 
#compare user numbers to winning numbers
#tell user if they got any numbers right
#tell user if they won or lost



print("welcome to bet slip checker app")
user_numbers = input("enter your betting numbers separated by a space: ")
numbers = user_numbers.split(" ")
winning_numbers = ["4", "8", "15", "16", "23", "42"]

if set(numbers) & set(winning_numbers):
    #first time l have seen this syntax
    #and code really efficiently checks for matches thanks stack overflow
    matched_numbers = set(numbers) & set(winning_numbers)
    print(f"you got {len(matched_numbers)} numbers right, they are {', '.join(matched_numbers)}")

else:
    print("sorry you got no numbers right, better luck next time")