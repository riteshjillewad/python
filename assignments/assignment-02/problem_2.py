######################################################################################
# Name:         problem_2.py
# Description:  Write a program that accepts two numbers from user and prints their:
#               Addition, Subtraction, Multiplication, Division
# Input:        Number
# Output:       Addition, Subraction, Multiplicaiton, Division
# Author:       Ritesh Jillewad
# Date:         14-06-2026
######################################################################################

def arithmetic(num1, num2):

    print("-------------------------------")
    print("---- ARITHMETIC OPERATIONS ----")
    print("-------------------------------")

    print("Addition       :", num1 + num2)
    print("Subtraction    :", num1 - num2)
    print("Multiplication :", num1 * num2)
    print("Division       :", num1 / num2)

    print("-------------------------------")


def main():
    num1 = None
    num2 = None

    print("Enter first number: ")
    num1 = int(input())

    print("Enter second number: ")
    num2 = int(input())

    arithmetic(num1, num2)


if __name__ == "__main__":
    main()