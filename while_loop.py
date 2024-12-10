# loops in python  >> loops are used to repeat instructions.

# while loop
i = 1
while i <= 5:
     print("hello")
     i +=1

## print numbers from 1 to 50.
x = 1
while x <= 50:
     print(x)
     x +=1
print("loop ended")

## print the number from 50 ti 1.
y = 50
while y >= 1:
     print(y)
     y -=1


## print the multiplication table of a number n.
n =3
i = 1
while i <=10:
     print("table of :", n*i)
     i +=1


## print the elements of the following list using a loop.
num = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(num):
     print(num[idx])  # num[0], num[1]...
     idx +=1


## search for a number x in this tuple using loop:
num = (1,4,9,16,25,36,49,64,81,100,25)

x = 25
a = 0  # initialization
while a < len(num):
     if(num[a]==x):
         print("found at index",a)
     a +=1