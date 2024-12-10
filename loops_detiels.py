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


# break keybord in python  >> used to terminate the loop when encountered.
i = 1
while i <= 5:
     print(i)
     if(i == 3):
         break
     i += 1


#continue keybord in python
i = 1
while i <= 10:
     if i == 5:
         i += 1
         continue  # skip
     print(i)
     i += 1


## print the odd and even number 1 to 100
i = 1
while i <= 100:
     if( i%2== 0): # odd number print(i%2 != 0)
         i += 1
         continue
     print(i)
     i +=1

## wap to find the sum of first n numbers.(using while)
n = 5

sum = 0
for i in range(1,n+1):
     sum += i
print("total sum =", sum)




# for loop >> loops are used for sequential traversal for traversing list,string ,tuple etc
num = [1,2,3,5]

for i in num:
     print(i)

str = "apnacollage"

for x in str:
      # if (x == 'g'):
         # break
      print(x)
else:
     print("end")

## print the element of the following list using a loop
nums = [1,4,9,16,25,36,49,64,81,100]

for i in nums:
     print(i)

## search for a number x in this tuple using loop
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
idx = 0
for i in nums:
     if (i == x):
         print("number found at idx",idx)
     idx +=1


# range()
# range(start, stop, step)
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])

for i in seq:
     print(i)

for i in range(10):  # (stop)
     print(i)

for i in range(2,10):  # (start,stop)
     print(i)

for i in range(2,10,2):   # (start,stop,step)
     print(i)

## print the even number with use range function:
for i in range(2,100,2):    # and odd number (1,100,2)
     print(i)

## print numbers from 1 to 100.
for i in range(1,100):
     print(i)

## print numbers from 100 to 1:
for i in range(100,0,-1):
     print(i)

## print the multiplication table of a number n.
for i in range(2,22,2):
     print(i)
    # or
n = int(input("enter number :"))

for i in range(1,11):
     print(n*i)


# pass statement  >> pass is a null statement that does nothing. it is used as a placeholder for future code.
for i in range(5):
     pass

if i > 4:
     pass

print("some useful work")


## wap to find the sum of first n numbers.
n = 5

sum = 0
for i in range(1,n+1):
     sum +=i

print("total sum :",sum)


## wap to find the factorial of first n number
n = 5

fact = 1
for i in range(1,n+1):
     fact *=i

print("factorial:",fact)


