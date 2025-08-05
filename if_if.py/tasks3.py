#student = {
   # "name": "legolas",
  #  "has_registered": True,
 #   "has_paid": True,
 #   "has_internet": False
#}
#only student that have registerd are eligible for axams. any student that has not
#register should be denied access with message "Access dinied".
#
#1. in as much as student have registerd, if the havent paid fees, the should be
#dinied access to exams with message "pay your fees".
#
#2. if the have paid and have internet access, message "Allow access", else "check your internet connection

student = {
    "name": "legolas",
    "has_registered": True,
    "has_paid": True,
    "has_internet": False
}

if not student["has_registered"]:
    print("Access denied")
elif not student["has_paid"]:
    print("Pay your fees")
elif not student["has_internet"]:
    print("Check your internet connection")
else:
    print("Allow access")

