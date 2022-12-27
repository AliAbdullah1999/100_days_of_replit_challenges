#a little bit of math
#generating bill including tip percentage
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
bill_you_owe = myBill / numberOfPeople
percentage_tip = int(input('Enter the percentage of tip for the waiter'))
percentage_amount = (percentage_tip / 100) * myBill
answer = percentage_amount + bill_you_owe
print("You all owe", answer)