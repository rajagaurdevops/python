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