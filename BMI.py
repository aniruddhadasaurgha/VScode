weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

BMI = weight_kg / (height_m ** 2)
print("Your BMI is:", BMI)

if BMI <= 18.4:
    print("You are underweight! You should eat more.")
elif BMI <= 24.9:
    print("You are healthy. Keep it up!")
elif BMI <= 29.9:
    print("You are overweight. You should exercise more.")
elif BMI <= 34.9:
    print("You have obesity class I. You should consult a doctor.")
elif BMI <= 39.9:
    print("You have obesity class II. You should consult a doctor immediately.")
else:
    print("You are extremely obese. You might die! Consult a doctor immediately and a bariatric surgery should be considered.")