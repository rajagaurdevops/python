# control structure
# if statement
a = 2
b = 3
if(a < b):
    print("a is less than b")

# output
a is less than b

# if-else statement
a = 12
b = 12
if (a<b):
    print("a is less than b")
else:
    print("a is equal to b") 

# output
  a is equal to b     


# if-elif-else statement
a = 12
b = 12
if (a < b):
    print("a is less than b")
elif (a > b):
    print("a is greater than b")
else:
    print("a is equal to b")        

# output
  a is equal to b

# nested-if statement
x = 10
if (x > 5):
    print("above 5")
    if (x > 20):
        print("above also above 20 !")
    else:
        print("but not above 20")

# output
    above 5
 but not above 20



# wap to check if a number entrerd by the user is odd or even

number = int(input("enter your number :"))

if(number % 2 == 0):
    print("even")
else:
    print("odd")



# wap to find the greatest of 3 number entered by the user

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter third number :"))

if(num1 > num2 and num1 > num3):
    print("first number is largest", num1)
elif(num2 > num1 and num2 > num3):
    print("second number is largest ", num2)
else:
    print("third number is largest", num3)



# wap to check if a number is a multiply of 7 or not

a = int(input("enter your number :"))

if(a % 7 == 0):
   print("multiply of 7 :", a)
else:
   print("not multiply of 7 :", a)