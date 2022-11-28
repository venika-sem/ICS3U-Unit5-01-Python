# Copyright (c) 2022 Venika Sem All rights reserved.
#
# Created by: Venika Sem
# Created on: Nov 2022
# This program calls function in python


def temperature():

    celsius = input("Enter a temperature (°C): ")

    try:
        print("")
        celsius_as_float = float(celsius)
        fahrenheit = 9 / 5 * celsius_as_float + 32
        print("{0}°C is equal to {1:.2f}°F.".format(celsius, fahrenheit))

    except ValueError:
        print("Invalid input, please try again.")

    print("\n\nDone.")


def main():
    temperature()


if __name__ == "__main__":
    main()
