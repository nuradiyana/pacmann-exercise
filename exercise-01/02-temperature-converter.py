def is_invalid_number(value) -> bool:
    """ Returns True if string is a number. """
    try:
        return float(value) < 0
    except ValueError:
        return True


def is_valid_temperature(value) -> bool:
    """ Returns True if string is a valid temperature. """
    temperatures = {'celsius', 'fahrenheit', 'kelvin'}

    return value.lower() in temperatures


def celsius_to_fahrenheit(celsius: float) -> float:
    """ Converts celsius to fahrenheit. """
    return (9 / 5 * celsius) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """ Converts fahrenheit to celsius. """
    return 5 / 9 * (fahrenheit - 32)


def celsius_to_kelvin(celsius: float) -> float:
    """ Converts celsius to kelvin. """
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """ Converts kelvin to celsius. """
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """ Converts kelvin to fahrenheit. """
    return kelvin * 9 / 5 - 459.67


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """ Converts fahrenheit to kelvin. """
    return (fahrenheit + 459.67) * 5 / 9


temperature_input = input("Masukan nilai temperatur : ")
if is_invalid_number(temperature_input):
    print("Not a valid input, please input number only")
    exit(1)

from_unit_input = input("Ubah dari (valid value : Celsius, Fahrenheit, Kelvin) : ")
if not is_valid_temperature(from_unit_input):
    print("Not a valid input, valid value is Celsius, Fahrenheit, Kelvin")
    exit(1)

to_unit_input = input("Ubah ke (valid value : Celsius, Fahrenheit, Kelvin) : ")
if not is_valid_temperature(to_unit_input):
    print("Not a valid input, valid value is Celsius, Fahrenheit, Kelvin")
    exit(1)

print("-" * 60)

temperature = float(temperature_input)
from_unit = from_unit_input.lower()
to_unit = to_unit_input.lower()

converted_temperature = temperature

if from_unit == 'celsius' and to_unit == 'fahrenheit':
    converted_temperature = celsius_to_fahrenheit(temperature)
elif from_unit == 'celsius' and to_unit == 'kelvin':
    converted_temperature = celsius_to_kelvin(temperature)
elif from_unit == 'fahrenheit' and to_unit == 'celsius':
    converted_temperature = fahrenheit_to_celsius(temperature)
elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
    converted_temperature = fahrenheit_to_kelvin(temperature)
elif from_unit == 'kelvin' and to_unit == 'celsius':
    converted_temperature = kelvin_to_celsius(temperature)
elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
    converted_temperature = kelvin_to_fahrenheit(temperature)

print(f"{temperature} {from_unit} is equal to {converted_temperature} {to_unit}")
