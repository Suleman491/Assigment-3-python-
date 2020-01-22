a=input("Enter Worked Hours(-1 to Quite): ")
b=input("Enter Hourly rate of the Employee:")
while(int(a)!= -1):
    salary=int(a)*int(b)
    print("Your Total Salary is: "+str(salary))
    a=input("Enter Worked Hours(-1 to Quite): ")
