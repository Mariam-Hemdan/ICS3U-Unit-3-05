#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This program display the month of the year that represents that number


def main():
    # this program display the month of the year that represents that number

    # input
    integer = int(input("Enter an integer from 1 to 12: "))

    # process
    if integer == 1:
        print(" January ")
    elif integer == 2:
        print(" Feburary ")
    elif integer == 3:
        print(" March ")
    elif integer == 4:
        print(" April ")
    elif integer == 5:
        print(" May ")
    elif integer == 6:
        print(" June ")
    elif integer == 7:
        print(" July ")
    elif integer == 8:
        print(" August ")
    elif integer == 9:
        print(" September ")
    elif integer == 10:
        print(" October ")
    elif integer == 11:
        print(" November ")
    elif integer == 12:
        print(" December ")

    else:
        print("Invalid")


if __name__ == '__main__':
    main()
