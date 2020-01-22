s1=input("Enter First Side of a trianle: ")
s2=input("Enter Second Side of a trianle: ")
s3=input("Enter Third Side of a trianle: ")
if((s1<s2+s3) and (s2<s1+s3) and (s3<s1+s2)):
    print("Yes. These three sides represent a triangle")
else:
    print("No. These three sides could not represent a triangle")

