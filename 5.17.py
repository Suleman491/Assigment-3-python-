nmbr=0
total=0.0
while(not int(nmbr) ==-1):
    nmbr = input("Product Number 1-5: ")
    qnt = input("Quantity Sold: ")
    if(int(nmbr)>=1 or int(nmbr)<=5):
        continue
    else:
        print("Invalid Entry")
if(int(nmbr)==1):
    total = float(total) + int(qnt) * 2.98
elif(int(nmbr)==2):
    total = float(total) + int(qnt) * 4.50
elif(int(nmbr)==3):
    total = float(total) + int(qnt) * 9.98
elif(int(nmbr)==4):
    total = float(total) + int(qnt) * 4.49
elif(int(nmbr)==5):
    total = float(total) + int(qnt) * 6.87
print("Total Retail Value of All Product is: "+str(total))

