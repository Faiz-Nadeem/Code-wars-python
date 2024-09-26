def Add(x,y):
    return x+y
def Multiply(x,y):
    return x*y
def Subtract(x,y):
    return x-y
def Divide(x,y):
    if(y !=0):return x/y
    else: return "Cannot divide by zero"

print("Select Operation")
print("1. ADD")
print("2. Multiply")
print("3. Subtract")
print("4. Divide")

num1= float(input("Enter number 1:"))
Choice= input("Enter operation 1/2/3/4 : ")
num2= float(input("Enter number 2:"))

if(Choice== '1'):
    print(f"{Add(num1,num2)}")
elif(Choice== '2'):
    print(f"{Multiply(num1,num2)}")
elif(Choice== '3'):
    print(f"{Subtract(num1,num2)}")
elif(Choice=='4'):
    print(f"{Divide(num1,num2)}")
else: "Invalid choice"