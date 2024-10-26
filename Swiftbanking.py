import datetime
print('welcome to Swiftbanking mobile app')
name="User"
balance=450000

print(" Welcome ", name)
print(f"you balance is : ${balance} ")
print("""press 1 to Deposit
press 2 to withdraw
press 3 to check balance
press 4 to exit""")
try:
    option=int(input("Enter your response: "))
    if option==1:
        amount=float(input("how much do you want to deposite: "))
        balance=balance+amount
        print(f" Credit alart !! ${amount}")
        print(f" Account Balance: ${balance:,}")
    elif option==2:
        amount=float(input("how much do you want to withdraw "))
        if amount>balance:
            print("insuficient balance")
        else:
            balance=balance-amount
            print(f" debit alart !! ${amount}")
            print(f" Account Balance: ${balance:,}")
    elif option==3:
        print(f" Account Balance: ${balance:,}")
    elif option==4:
        print("thank you for using whales atm")
    else:
        print("invalid input try again")
except:
    print("input valid a single number")
finally:
    print("thank you for using Swiftbanking mobile app")
    print(datetime.datetime.now())

