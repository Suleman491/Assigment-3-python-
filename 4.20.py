passstd=0
failstd=0
std=1
a=input("Enter Result(1=Pass , 2=fail): ")
while(std<10):
    a = input("Enter Result(1=Pass , 2=fail): ")
    std+=1
    if(int(a)==1):
        passstd += 1
    elif(int(a)==2):
        failstd += 1
    else:
        print("Invalid result!")
print("Pass Students: "+str(passstd))
print("Fail Students: "+str(failstd))
if(passstd>8):
    print("Bonus to Instructor")

