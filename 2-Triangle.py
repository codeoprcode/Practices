
print("Do you want to draw a triangle with these Sides?")

a = float(input("Please enter side one: "))
b = float(input("Please enter side two: "))
c = float(input("Please enter side three: "))

if a < b + c and b < a + b and c < a + b :
    print("You right.")
else:
    print("You can't draw")