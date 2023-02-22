
print("See students status")

a = input("Please enter student name: ")
b = input("Please enter student gender with male & female: ")

c = float(input("Please enter score one= "))
d = float(input("Please enter score two= "))
e = float(input("Please enter score three= "))

avr = ( c + d + e) / 3

if b == "male":
    if avr >= 17:
        print("Educational status of Mr", a, "is Great")
    elif 17 > avr >= 12:
        print("Educational status of Mr", a, "is Normal")
    else:
        print("Educational status of Mr", a , "is Fail")


if b == "female":
    if avr >= 17:
        print("Educational status of Mrs", a, "is Great")
    elif 17 > avr >= 12:
        print("Educational status of Mrs", a, "is Normal")
    else:
        print("Educational status of Mrs", a , "is Fail")
