count=0
a=input("Enter Distance in Miles(-1 to Quite): ")
b=input("Enter Total Gallons: ")
while(int(a)!=-1):
    count+=1
    MPG=int (a)/int (b)
    Average=int(MPG)/int(count)
    print("Mileage per Gallon for This Trip: "+str (MPG))
    print("Total mileages per Gallon: "+str(Average))
    a = input("Enter Distance in Miles(-1 to Quite):" )
