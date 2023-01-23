import math
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("\n") #skipping a line
#the different things the program does
print("investment - to calculate the amount of interest you'll earn on interest")
print("bond - to calculate the amount you'll have to pay on a home loan")

menu = input("Enter your choice: ") #user inputs what they want to calculate
if menu.lower() == "investment":
  print("Your choice is: " + menu) #printing their choice
  deposit = int(input("Enter your deposit amount: "))
  interest_rate = float(input("Enter the interest as a percentage without '%': "))
  years = int(input("Enter the number of years of investment: "))
  interest = input("Simple or compound interest: ")
  print(" ")
  interest_in_decimals = interest_rate / 100
  if interest.lower() == "simple": #if they go with the simple interest option
    amount = deposit * (1 + interest_in_decimals * years)
    print("The total amount is R" + str(amount)) #the amount they will get at the end
  if interest.lower() == "compound": #if they gp with the compound interest option
    amount = deposit * math.pow((1 + interest_in_decimals), years)
    print("The total amount is R" + str(amount)) #the amount they will get at the end
print(" ")
if menu.lower() == "bond":
  print("Your choice is: " + menu)
  value = int(input("Enter value of house without the R: "))
  interest_rate = float(input("Enter the interest rate without the %: "))
  months = int(input("Enter number of months to pay it back: "))
  monthly_interest_rate = (interest_rate / 100) / 12 #dividing the annual rate by 12 months
  monthly_repayment = (monthly_interest_rate * value) / (1 - (1 + monthly_interest_rate)**(-months))
  print("Your monthly repayment will be R" + str(monthly_repayment)) #printing how much they will pay monthly
else:
  print("Invalid, please try again.") #if the user doesn't choose any of the options