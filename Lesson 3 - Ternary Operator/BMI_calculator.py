height = int(input("Enter the calculator height (in inches): "))
weight = int(input("Enter the calculator weight (in pounds): "))

BMI = (weight / (height * height)) * 703
print(BMI)

status = (
    "Underweight"
    if BMI < 18.5
    else (
        "Normal"
        if 18.5 <= BMI <= 24.9
        else "Overweight" if 25 <= BMI <= 29.9 else "Obese"
    )
)
print(f"category = {status}")

if status == "Normal":
    print("Recommendation: Maintain weight")
    print("Health Risk: Low")
elif status == "Overweight":
    print("Recommendation: Lose weight")
    print("Health Risk: Low")
    
