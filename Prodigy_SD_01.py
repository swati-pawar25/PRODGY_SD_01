#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value, unit):
    if unit == "C":
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")
    elif unit == "F":
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value}°F is {celsius:.2f}°C and {kelvin:.2f}K")
    elif unit == "K":
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

# User input
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

convert_temperature(temperature, unit)


# In[ ]:




