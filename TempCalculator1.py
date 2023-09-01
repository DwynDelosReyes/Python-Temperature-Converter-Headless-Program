"""
Headless Basic Python Temperature Calculator
First Attempt
Author: Dwyn Delos Reyes
"""

choice = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

choice = choice.upper()  # Convert the choice to uppercase to ensure consistency

# provides a choice between Celsius or Fahrenheit
if choice == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif choice == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")

# happens if the user doesn't follow the choices
else:
    print(f"{choice} is an invalid unit of measurement.")

"""
Headless Basic Python Temperature Calculator
First Attempt
Author: Dwyn Delos Reyes
"""
