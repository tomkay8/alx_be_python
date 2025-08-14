FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using a global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using a global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Ask user for the temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        # Ask for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value." if "could not convert" in str(e) else e)

if __name__ == "__main__":
    main()

