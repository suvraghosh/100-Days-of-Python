
print("\tWelcome to the rollercoaster.!")
height=int(input("What is your height in cm? "))
bill=0
if height>=120:
    print("You can ride the rollercoaster.")
    age=int(input("What is your age? "))
    if age<12:
        bill=10
        print("Child tickets are ₹10")
    elif age<=18:
        bill=20
        print("Youth tickets are ₹20")
    else:
        bill=30
        print("Adult tickets are ₹30")

    photo=input("Do you want a photo taken? Y or N. ")
    if photo == "Y":
        bill += 5

    print(f"Your final bill is ₹{bill}")
else:
    print()