nmbr=input("Enter Five Numbers Between 1 to 9: ")
for i in range(1,5):
    i=i+1
    if(int(nmbr)<1 or 9< int(nmbr)):
        print("Number is out of Range")
    else:
        for j in range(1,2):
            j=j+i
            for k in range(1,int(nmbr)):
                k=k+1
            print(str(k)+str(k))
