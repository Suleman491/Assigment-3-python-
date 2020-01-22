m=input("Enter Minutes: ")
h=input("Enter Hours: ")
d=input("Enter Days: ")

def cal(m,h,d):
    return int(m)+int(h)*60+int(d)*360

print(str(cal(m,h,d)))

