######################################################################################
# Name:         problem_3.py
# Description:  Write a program that takes user's name and age to display
# Input:        name, age
# Output:       Hello <name>, you will turn <age + 1> next year
# Author:       Ritesh Jillewad
# Date:         14-06-2026
######################################################################################

def display(name, age):

    print(f"Hello {name}, you will turn {age + 1} next year.")


def main():
    name = None
    age = None

    print("Enter name: ")
    name = input()

    print("Enter age: ")
    age = int(input())

    display(name, age)

if __name__ == "__main__":
    main()