principle=1000
print("Year"+"       5%"+"        6%"+"        7%"+"        8&"+"        9%"+"        10%")
for i in range(1,10):
    i=i+1
    for a in range(5,10):
        a=a+1
        amount=principle*(pow(1+a/100,i))
        print(str(i)+"       "+str(amount)+"       "+str(amount)+"       "+str(amount)+"       "+str(amount)+"       "+str(amount)+"       "+str(amount))

