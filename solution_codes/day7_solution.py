#pracising nested if and elif
order = input('What would you like to have: pizza or hamburger')
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  elif cheese == 'No': 
    print("No cheese it is.")
elif order == 'pizza':
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
else:
  print("Your pizza will not have pepperoni")
