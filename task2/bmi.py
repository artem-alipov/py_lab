
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in santimeters: "))

bmi = weight / (height/100) ** 2
bmi_min, bmi_max = 16, 50
bmi_scale = ''.join(['=','|'][i==round((bmi-bmi_min)*33/(bmi_max-bmi_min))] for i in range(34))

print("Your BMI is {:.2f}".format(bmi))
print("BMI: 16 {} 50".format(bmi_scale, bmi_min, bmi_max))
