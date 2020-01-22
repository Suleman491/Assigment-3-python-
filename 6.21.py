a=input("Integer number (0 to end): ")
def multiple3(nmbr):
    return not(nmbr%3)
while(True):
    a = input("Integer number (0 to end): ")
    if(not int(a)):
        break
        print(str(a)+" is not Multiple of "+str(multiple3(int(a)))+ str(nmbr))
    else:
        print(str(a) + " is Multiple of " + str(multiple3(int(a))))

