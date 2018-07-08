print("enter two number")
x=input("enter first number  ")
y=input("enter second number ")
while(True):
 try:
    if(float(x)>float(y)):
       print(str(x) +" is greater")
       
    else:
       print(str(y) +"  is greater")
       
 except :
    print("you did not enter numeric value") 
    print("please input again")
    x=input("enter first number")
    y=input("enter second number")
 else:
    print("two numbers compared successfully")
    break
 finally:
    print("your program executed")
