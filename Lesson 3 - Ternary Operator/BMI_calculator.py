weight = int(input("Enter the calculator weight (in pounds): "))
height = int(input("Enter the calculator height (in inches): "))

BMI = (weight/height^2) * 703

status = "Underweight" if BMI < 18.5 else "Normal" if 18.5 <= BMI <= 7