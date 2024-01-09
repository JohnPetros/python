# Task 13 - Write a script that converts a temperature entered in °C to °F.

temperatureInCelcius = float(input('Input the temperature in °C: '))

temperatureInFahrenheit = temperatureInCelcius * 9 / 5 + 32 

print(f'The temperature of  {temperatureInCelcius:.1f}°C, corresponds to {temperatureInFahrenheit:.1f}°F')

