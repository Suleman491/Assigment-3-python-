a=input("Enter the Account Number(-1 to quite):")
b=input("Enter the Beginning Balance:")
c=input("Enter Total Charges:")
d=input("Enter Total Credits:")
e=input("Enter Credits Limit:")

while(int(a)!= -1):
    nblnce = int(b + c) -int(d)
    print("New Balance is: "+str (nblnce))
    print("Account Number is: "+str(a))
    print("Credit Limit is: "+ str(e))

    if(int(e)< int(nblnce)):
        print("Credit Limit Exceeded")
    a=input("Enter the Account Number(-1 to quite):")

