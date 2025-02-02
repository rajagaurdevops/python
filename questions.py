# three numbers in the largest number print

program-
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a > b) and (a > c):
    print(f"The largest number is: {a}")
elif (b > a) and (b > c):
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")


# write a python program to check that given year is leap year or not

year = int(input("Enter a year: "))

if (year % 4 == 0):

    if (year % 100 == 0):

        if (year % 400 == 0):

            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# write a python program to check whether the given number is prime or not

num = int(input("enter number :"))

for i in range(2, num):
    if(num % i == 0):
        print(num, "is not a prime number :")
        break
else:
    print(num, "is a prime number ")


# write a python program to swap two numbers without using third variable

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("BEFORE SWAPING")

print("first number :", a)
print("second number :", b)

# Swapping without using a third variable
a = a + b
b = a - b
a = a - b

print("AFTER SWAPING")

print("first number :", a)
print("second number :", b)


# write a python program to swap two numbers using third variable 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("BEFORE SWAPING")

print("first number :", a)
print("second number :", b)

# Swapping without using a third variable
temp = a
a = b
b = temp

print("AFTER SWAPING")

print("first number :", a)
print("second number :", b)


