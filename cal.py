def add(x,y):
    return (x + y)

def sub(x,y):
 return  (x - y )

def multiply(x,y):
    return (x * y )

def divide(x,y):
  return (x  /  y )


def power(x,y):
   return pow( x ,  y )

print ("Calculator  Select Operations")
print  ("1:add")
print ("2:sub")
print  ("3:multiply")
print  ("4:Divide")
print  ("5:power")
choice =input("Enter choice(1/2/3/4/5)")
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))

if choice =='1':
    print (num1, "+", num2, add(num1,num2))
elif choice =='2':
    print (num1, "-", num2, sub(num1,num2))
elif     choice =='3':
    print (num1, "*", num2, multiply(num1,num2))

elif choice =='4':
    print (num1, "+", num2, divide(num1,num2))
elif  choice=="5":
 print (num1 ,"",num2 , power(num1,num2))
else :
     print ("Invalid Number")

