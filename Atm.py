class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is $50000")

    def withdrawl(self,amount):
        if amount <= 50000:
            print(" You dont have enough money")
            
        else:
            new_amount = 50000 - amount
            print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

            
        

def main():
    Card_number = input("insert your card number: ")
    pin_number  = input("enter your pin number:  ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose what you want to do ")
    print("1.Your Balance   2.Withdraw money")
    activity = int(input("enter activity number: "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount: "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()