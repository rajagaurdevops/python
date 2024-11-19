## print the multiplication table of a number n.(using while)

n =3
i = 1
while i <=10:
     print("table of :", n*i)
     i +=1

## print the multiplication table of a number n.

for i in range(2,22,2):
     print(i)
    # or
n = int(input("enter number :"))

for i in range(1,11):
     print(n*i)

## waf to find the factorial of n.(n is the parameter)

def cal_fact(n):
     fact = 1
     for i in range(1,n+1):
          fact *= i
     print(fact)

cal_fact(5)
