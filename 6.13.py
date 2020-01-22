def rnd():
    return int(nmbr) + 0.5
for i in range(1,5):
    i+=1
    nmbr = input("Enter Number: ")
    print("Nearest integer for "+str(i)+" is "+str(rnd()))
