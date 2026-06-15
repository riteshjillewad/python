######################################################################################
# Name:         problem_1.py
# Description:  Write a program to display: Value, Type and Memory Address
# Input:        Number
# Output:       Value, Type and Memory Address
# Author:       Ritesh Jillewad
# Date:         14-06-2026
######################################################################################

def displayKundali(num):

    print("=" * 25)
    print("      KUNDALI")
    print("=" * 25)

    print("Value :", num)
    print("Type  :", type(num))
    print("Memory:", id(num))

    print("=" * 25)

def main():

    num = None
    num = int(input("Enter number: "))
    displayKundali(num)

if __name__ == "__main__":
    main()
