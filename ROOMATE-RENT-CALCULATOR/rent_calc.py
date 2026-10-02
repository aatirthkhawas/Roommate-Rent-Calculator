print("=====ROOMATE RENT CALCULATOR=====")
#NAME OF THE ROOMATES:
roomate_1 = input("Roomate name =")
roomate_2 = input("Roomate name =")
roomate_3 = input("Roomate name =")

#ALL EXPENSES:
house_rent = float(input("Cost of living:"))
electricity = float(input("Electricity bill:"))
Food = float(input("Online food orders:"))
other_expenses = float(input("other expenses:"))

print()

#TOTAL EXPENSES:
Total_cost = house_rent + electricity + Food + other_expenses
per_person = Total_cost/3


#DASHBBOARD: 
print("=====DASHBOARD=====")
print("House Rent:",house_rent)
print("Electricity:",electricity)
print("Food Orders:",Food)
print("Other Expenses:",other_expenses)

print()

print("=====EXPENSES!!!=====")
#FINAL RESULT:
print(f"Total Rent is {round(Total_cost)}")
print(f"{roomate_1} pays:{round(per_person)}") 
print(f"{roomate_2} pays:{round(per_person)}") 
print(f"{roomate_3} pays:{round(per_person)}") 

print()

print("====THANKYOU!====")