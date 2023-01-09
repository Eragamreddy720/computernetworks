age=int(input("enter the age"))
v=0
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")
    v=18-age
print("you are eligible to vote in ",v,"years")
