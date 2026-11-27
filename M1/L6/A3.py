def calculate_bmi(weight_kg: float, height_m: float) -> float:
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def main() -> None:
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters (e.g., 1.75): "))
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        print(f"BMI: {bmi:.1f}")
        print(f"Category: {category}")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
