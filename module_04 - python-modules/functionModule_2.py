import marvellous as mi

def main():
    print("Enter first number: ")
    value1 = int(input())

    print("Enter second number: ")
    value2 = int(input())

    ret = mi.addition(value1, value2)                      
    print("Sum:", ret)

if __name__ == "__main__":
    main()