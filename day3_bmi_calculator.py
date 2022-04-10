height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height**2,0)

if bmi > 35:
  print("You are clinically obsese")
elif bmi > 30:
  print("You are obese")
elif bmi > 25:
  print("You are slightly overweight")
elif bmi > 18.5:
  print("You have a normal weight")
else:
  print("You are underweight")

