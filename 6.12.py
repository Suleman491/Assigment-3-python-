print("Car's"+"        "+"Hour's"+"        "+"Charge's")
def calculation():
    if(int(hrs)<=3):
        return int(hrs) * 20
    elif(int(hrs)>3):
        return int(hrs)*20+5
def thrs(totalhrs=0):
    return totalhrs+int(hrs)
for car in range(0,3):
    car+=1
    hrs=input(" ")
    print(str(car) + "               " + str(thrs()) + "            " + str(calculation()))

