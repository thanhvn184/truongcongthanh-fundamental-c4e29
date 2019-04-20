H = int(input("Enter your height(cm): "))
W = int(input("Enter your weight(kg): "))
HM = H/100
BMI = W/(HM*HM)
print("Your BMI is:", BMI )
if BMI<16:
    print("You are severely underweight!")
elif BMI<18.5:
    print("You are underweight.")    
elif BMI<25:
    print("You are normal. Congrats!")
elif BMI<30:
    print("You are overweight.")
else:
    print("You are obese hahahaha")            