a=input("Number (1 to 32767): ")
d=1
def seprate(n):
    while(n/d):
        return d*10
    while(d>1):
       print(str((n%d)/(n/d)))
    return d/10
while(int(a)<1 or int(a)>32767):
    a = input("Number (1 to 32767): ")
print(str(seprate(int(a)))+"  ")

