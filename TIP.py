print("\t\t\tWelcome to TIP calculator!!!\n")

amount = float(input("Enter the amount of bill :"))
tip = float(input("Enter the percentage of tip :"))

bill = (amount*t)/100 + amount

numbers = float(input("No. of people to divide it into :"))
split = bill/numbers

print(f"Total individual amount to be paid is {split}\n")