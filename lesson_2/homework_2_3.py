# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C

# type your code here
temperature_fahrenheit = input("Please enter the temperature right now in Fahrenheit: ")
celsius_formula = (int(temperature_fahrenheit) - 32) * 5/9
result_temperature = celsius_formula
print("The current temperature is" , result_temperature , "C")