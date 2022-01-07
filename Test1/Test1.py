print(" *** BMI ***")
x , y = input("Enter your weight(kg) and height(m) : ").split()
i=float(x)
j=float(y)
BMI = i/(j*j)
if BMI < 18.5:
    print("Your status is : Below normal weight.")
elif BMI <=18.5 or BMI<25:
    print("Your status is : Normal weight.")
elif BMI <=25 or BMI <30:
    print("Your status is : Overweight.")
elif BMI <=30 or BMI <35:
    print("Your status is : Case I Obesity.")
elif BMI<=35 or BMI<40:
    print("Your status is : Case II Obesity.")
elif BMI >=40:
    print("Your status is : Case III Obesity.")
