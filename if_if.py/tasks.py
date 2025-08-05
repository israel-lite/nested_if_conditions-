#MOVIE TICKET DISCOUNT:
#
# you are building a movie ticketing system.
#instrutions: ask user for their age:
#1. person 18 or older can buy a ticket.
#out "can buy ticket"
#
#if they are 60 orolder, they get "senior discount":
#output: "senior discount"
#
#if they are under 18 and 12rs or older, the can buy teen ticket.
#output: teen ticket
#otherwise, the can buy "kids ticket"

# MOVIE TICKET DISCOUNT SYSTEM

age = int(input("Enter your age: "))

if age >= 18:
    print("Can buy ticket")

    if age >= 60:
        print("Senior discount")

elif age >= 12:
    print("Teen ticket")

else:
    print("Kids ticket")


