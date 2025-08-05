#SMARTPHONE PURCHASE:
#
#ask user to input budget
#
#1. check if the budget is atleast $500, if it is , check if the budget is $1000 or more. then
#recommend "Google pixle 9pro", otherwise, recommend "IPhone"
#
#2. if budget is below $500, if it is, and atleast $200. then recommend "Redmi"

# SMARTPHONE PURCHASE

budget = float(input("Enter your budget in $: "))

if budget >= 500:
    if budget >= 1000:
        print("We recommend: Google Pixel 9 Pro")
    else:
        print("We recommend: iPhone")

elif budget >= 200:
    print("We recommend: Redmi")

else:
    print("Sorry, no smartphones available in this budget range so i advice you not to eat for two week an save more money for Iphone.")

