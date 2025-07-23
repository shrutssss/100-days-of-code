print("Welcome to Tip Calculator!\n")

#Taking Inputs: bill, tip, people using input() function.
#Here, we put int() before input function as the input has to be of integer type.
bill=int(input("What was the total bill?\n"))
tip_percent=int(input("How much tip would you like to give: 10, 12 or 15%? (type without %)\n"))
number_of_people=int(input("How many people are splitting the bill?\n"))

#Splitting of bill
bill_per_person=(bill/number_of_people)*(1+(tip_percent/100))

#Round off the bill split by 2 decimal places using round() function:
final_bill=round(bill_per_person,2)

print(f"Each person should pay: {final_bill}")
