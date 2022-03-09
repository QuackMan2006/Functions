def check_BMI(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif BMI <25:
        return "Normal"
    elif BMI <30:
        return "Overweight"
    else:
        return "Obese"

#Main routine
get_BMI = float(input("Enter BMI: "))
print(f"With a BMI of {get_BMI} your status is {check_BMI(get_BMI)}")
