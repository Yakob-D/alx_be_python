FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return fahrenheit

temperature = float(input("Enter the temperature to convert: "))
check = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if check == 'F':
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
elif check == 'C':
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
else:
    print("Invalid input.")
