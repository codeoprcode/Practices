import math

print('Dear user, This is your calculator')

print('sqrt')
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")
print('Please write one of the operations above:')

op = input()

if op == "sqrt" or op == "factorial" :
    a = float(input("please enter number: "))

else:
    a = float(input("please enter degree: "))
    
    

if op == "sqrt":
    if a >= 0:
        r = math.sqrt(a)
    else :
        r="Please enter positive number"   

elif op == "sin":
    r = math.sin(a)

elif op == "cos":
    r = math.cos(a)

elif op == "tan":
    if a == 90 or a == 270:
        r = "This is undefined"
    else :
        b = a * math.pi / 180    
        r = math.tan(b)

elif op == "cot":
    if a == 180 or a == 0 or a == 360:
        r = "This is undefined"
    else :    
        b = a * math.pi / 180
        r = 1 / math.tan(b)

elif op == "factorial":
    if a == 0:
        r = 1
    elif a >= 1:
        r = math.factorial(a)
    else :
        r="Please enter positive number"

print("Your result= ", r)
