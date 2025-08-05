#1. you try to withdraw money from Nigerian ATM.
#2. the ATM has only $1000 notes and you have $10,000 in your account.
#3. the machine allows withdraw only if the amount requested is less than or equal
#to your balance.
#4. the user enters the amount.
#
#5. your program should decide:
#6. whether to allow the transaction?
#7. or deny it with a message:
#"Insufficient funds or invalid amount"?

# ATM SETTINGS
atm_note = 1000     
user_balance = 1000     

# USER INPUT
:
    amount = int(input("Enter amount to withdraw (₦): "))

    # CHECK CONDITIONS
    if amount <= user_balance and amount % atm_note == 0:
        print(f"Transaction approved. You withdrew ₦{amount}.")
        user_balance -= amount
        print(f"Remaining balance: ₦{user_balance}")
    else:
        print("Insufficient funds or invalid amount. Only ₦1000 notes allowed.)

except ValueError:
    print("Invalid input. Please enter a numeric amount.)

