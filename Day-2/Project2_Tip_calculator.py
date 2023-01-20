
print("\tCalculate the bill of Restaurant!!")

bill=float(input("Enter the total bill price: ₹"))
tip=int(input("Want to give some tips? 10,15,20 ₹"))
people=int(input("Enter the total number of people: "))
tip_amount=bill*tip/100
total_bill_amount=bill+tip_amount
individual_payment=round(total_bill_amount/people,2)

print(f"You will have to pay only: ₹{individual_payment}")