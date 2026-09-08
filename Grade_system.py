# Student Grade System

try:
    # Get mark from the user
    mark = float(input("Enter your mark (0-100): "))

    # Check whether the mark is within the valid range
    if mark < 0 or mark > 100:
        print("Invalid mark. Please enter a number between 0 and 100.")

    # Determine the grade
    elif mark >= 90:
        print(f"Mark: {mark:g} -> Grade: A")

    elif mark >= 80:
        print(f"Mark: {mark:g} -> Grade: B")

    elif mark >= 70:
        print(f"Mark: {mark:g} -> Grade: C")

    elif mark >= 60:
        print(f"Mark: {mark:g} -> Grade: D")

    else:
        print(f"Mark: {mark:g} -> Grade: E")

# Handle non-numeric input
except ValueError:
    print("Invalid input. Please enter a valid number between 0 and 100.")