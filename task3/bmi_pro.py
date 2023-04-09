while True:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in santimeters: "))
    age = int(input("Enter your age in years: "))
    gender = input("Enter your gender (M/F): ")

# Calculate BMI and create dynamic console scale
    bmi = weight / (height/100) ** 2
    bmi_min, bmi_max = 16, 50
    bmi_scale = ''.join(['=','|'][i==round((bmi-bmi_min)*33/(bmi_max-bmi_min))] for i in range(34))

# Display BMI and dynamic console scale
    print("Your BMI is {:.2f}".format(bmi))
    print("BMI: 16 {} 50".format(bmi_scale, bmi_min, bmi_max))

    if bmi < 18.5:
        print("BMI indicates underweight.")
        if age < 25:
            if gender == "M":
                print("Recommendations: Increase caloric intake and engage in resistance training to build muscle mass.")
            elif gender == "F":
                print("Recommendations: Increase caloric intake and engage in resistance training to build muscle mass.")
        elif 25 <= age < 35:
            if gender == "M":
                print("Recommendations: Increase caloric intake and engage in resistance training to build muscle mass.")
            elif gender == "F":
                print("Recommendations: Increase caloric intake and engage in resistance training to build muscle mass.")
        elif 35 <= age < 45:
            if gender == "M":
                print("Recommendations: Increase caloric intake and engage in resistance training to build muscle mass. Consider hormone replacement therapy for bone health.")
            elif gender == "F":
                print("Recommendations: Increase caloric intake and engage in resistance training to build muscle mass. Consider hormone replacement therapy for bone health.")
        elif 45 <= age < 55:
            if gender == "M":
                print("Recommendations: Increase caloric intake and engage in resistance training to build muscle mass. Consider hormone replacement therapy for bone health.")
            elif gender == "F":
                print("Recommendations: Increase caloric intake and engage in resistance training to build muscle mass. Consider hormone replacement therapy for bone health.")
    elif 18.5 <= bmi < 25:
        print("BMI indicates normal weight.")
        if age < 25:
            if gender == "M":
                print("Recommendations: Maintain current weight and engage in regular exercise to improve overall fitness.")
            elif gender == "F":
                print("Recommendations: Maintain current weight and engage in regular exercise to improve overall fitness.")
        elif 25 <= age < 35:
            if gender == "M":
                print("Recommendations: Maintain current weight and engage in regular exercise to improve overall fitness.")
            elif gender == "F":
                print("Recommendations: Maintain current weight and engage in regular exercise to improve overall fitness.")
        elif 35 <= age < 45:
            if gender == "M":
                print("Recommendations: Maintain current weight and engage in regular exercise to improve overall fitness. Consider hormone replacement therapy for bone health.")
            elif gender == "F":
                print("Recommendations: Maintain current weight and engage in regular exercise to improve overall fitness. Consider hormone replacement therapy for bone health.")
        elif 45 <= age < 55:
            if gender == "M":
                print("Recommendations: Maintain current weight and engage in regular exercise to improve overall fitness. Consider hormone replacement therapy for bone health.")
            elif gender == "F":
                print("Recommendations: Maintain current weight and engage in regular exercise to improve overall fitness. Consider hormone replacement therapy for bone health.")
    elif 25 <= bmi < 30:
        print("BMI indicates overweight.")
        if age < 25:
            if gender == "M":
                print("Recommendations: Increase exercise and reduce caloric intake to achieve weight loss. Consider consulting a nutritionist for personalized meal planning.")
            elif gender == "F":
                print("Recommendations: Increase exercise and reduce caloric intake to achieve weight loss. Consider consulting a nutritionist for personalized meal planning.")
        elif 25 <= age < 35:
            if gender == "M":
                print("Recommendations: Increase exercise and reduce caloric intake to achieve weight loss. Consider consulting a nutritionist for personalized meal planning.")
            elif gender == "F":
                print("Recommendations: Increase exercise and reduce caloric intake to achieve weight loss. Consider consulting a nutritionist for personalized meal planning.")
        elif 35 <= age < 45:
            if gender == "M":
                print("Recommendations: Increase exercise and reduce caloric intake to achieve weight loss. Consider consulting a nutritionist for personalized meal planning. Consider hormone replacement therapy for bone health.")
            elif gender == "F":
                print("Recommendations: Increase exercise and reduce caloric intake to achieve weight loss. Consider consulting a nutritionist for personalized meal planning. Consider hormone replacement therapy for bone health.")
        elif 45 <= age < 55:
            if gender == "M":
                print("Recommendations: Increase exercise and reduce caloric intake to achieve weight loss. Consider consulting a nutritionist for personalized meal planning. Consider hormone replacement therapy for bone health.")
            elif gender == "F":
                print("Recommendations: Increase exercise and reduce caloric intake to achieve weight loss. Consider consulting a nutritionist for personalized meal planning. Consider hormone replacement therapy for bone health.")
    elif bmi >= 30:
        print("BMI indicates obesity.")
        if age < 25:
            if gender == "M":
                print("Recommendations: Engage in regular exercise and follow a medically supervised weight loss program. Consider consulting a nutritionist for personalized meal planning.")
            elif gender == "F":
                print("Recommendations: Engage in regular exercise and follow a medically supervised weight loss program. Consider consulting a nutritionist for personalized meal planning.")
        elif 25 <= age < 35:
            if gender == "M":
                print("Recommendations: Engage in regular exercise and follow a medically supervised weight loss program. Consider consulting a nutritionist for personalized meal planning.")
            elif gender == "F":
                print("Recommendations: Engage in regular exercise and follow a medically supervised weight loss program. Consider consulting a nutritionist for personalized meal planning.")
        elif 35 <= age < 45:
            if gender == "M":
                print("Recommendations: Engage in regular exercise and follow a medically supervised weight loss program. Consider consulting a nutritionist for personalized meal planning. Consider hormone replacement therapy for bone health.")
            elif gender == "F":
                print("Recommendations: Engage in regular exercise and follow a medically supervised weight loss program. Consider consulting a nutritionist for personalized meal planning. Consider hormone replacement therapy for bone health.")
        elif 45 <= age < 55:
            if gender == "M":
                print("Recommendations: Engage in regular exercise and follow a medically supervised weight loss program. Consider consulting a nutritionist for personalized meal planning. Consider hormone replacement therapy for bone health.")
            elif gender == "F":
                print("Recommendations: Engage in regular exercise and follow a medically supervised weight loss program. Consider consulting a nutritionist for personalized meal planning. Consider hormone replacement therapy for bone health.")
    answer = input("Would you like to check again? (Y/N)")
    if answer.lower() != "y":
        break       