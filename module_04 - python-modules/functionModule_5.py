from marvellous import *

def main():
    print("Enter first number: ")
    value1 = int(input())

    print("Enter second number: ")
    value2 = int(input())

    ret = addition(value1, value2)
    print("Addition is:", ret)

    ret = subtraction(value1, value2)
    print("Subtraction is:", ret)

if __name__ == "__main__":
    main()