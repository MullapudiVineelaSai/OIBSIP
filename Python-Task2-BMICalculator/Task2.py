def bmi_calculator():
    print("=== BMI Calculator ===")
    
    try:
        # User input
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kg: "))

        # Validation
        if height <= 0 or weight <= 0:
            print("Error: Height and Weight should be greater than 0")
            return

        # BMI Calculation
        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")

        # Category Check
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"You are in: {category} category")
    
    except ValueError:
        print("Error: Please enter valid numbers only")

# Run the function
bmi_calculator()
