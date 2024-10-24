def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("Select a conversion (1-6): "))
   
    if choice in [1, 3]:
        temp = float(input("Enter temperature in Celsius: "))
        if choice == 1:
            print(f"{temp} °C = {celsius_to_fahrenheit(temp)} °F")
        else:
            print(f"{temp} °C = {celsius_to_kelvin(temp)} K")
   
    elif choice in [2, 5]:
        temp = float(input("Enter temperature in Fahrenheit: "))
        if choice == 2:
            print(f"{temp} °F = {fahrenheit_to_celsius(temp)} °C")
        else:
            print(f"{temp} °F = {fahrenheit_to_kelvin(temp)} K")

    elif choice in [4, 6]:
        temp = float(input("Enter temperature in Kelvin: "))
        if choice == 4:
            print(f"{temp} K = {kelvin_to_celsius(temp)} °C")
        else:
            print(f"{temp} K = {kelvin_to_fahrenheit(temp)} °F")
   
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()