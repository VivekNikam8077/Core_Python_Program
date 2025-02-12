# Python program to check if a year is a leap year or not

# Input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year or not
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")


"""Input from the user: 2020
   Output :It is a leap year"""
