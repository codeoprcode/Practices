print("Calculate your BMI indicator")

a = float(input("Please enter your weight(kg)= "))
b = float(input("Please enter your height(m)= "))
BMI= a / b**2

if BMI < 18.5:
    print("You are Underweight")
elif 18.5 <= BMI < 24.9:
    print("You are Normal Weight")
elif 25 <= BMI < 29.9:
    print("You are Overweight")
elif 30 <= BMI < 34.9:
    print("You are Obesity")
elif 35 <= BMI < 39.9:
    print("You are Extreme Obesity")

