class bankatm(object):
    def __init__(self,pinnumber,cardnumber):
        self.pinumber = pinnumber
        self.cardnumber = cardnumber

    def cashwithdrawl(self):
        print("cash is succesfully withdrawed")

    def balanceEnquiry(self):
        print("balance is printed")        

def main():
    card_number = input("enter your card number")
    pin_number = input("enter your pin number")
    new_user =bankatm(card_number,pin_number)
    print(new_user.card_number)

if __name__=="__main__":
    main()