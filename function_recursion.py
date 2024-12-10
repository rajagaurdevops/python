# functions >> block of statement that perform a specific task:
def calc_sum(a, b):
      sum = a+b
      print(sum)
      return sum

calc_sum(5,10)

calc_sum(5,5)

def calc_sum(a,b):  # parameters
      return a+b

sum = calc_sum(4,4) # functin call
print(sum)     

#  and
def print_name():
      print("rajagaur")

print_name()
print_name()

## average of 3 numbers
def cals_avg(a,b,c):
      sum = a+b+c
      avg = sum / 3
      print(avg)
      return avg

cals_avg(5,5,5)

def multiple_num(a,b):
        sum = a*b
        print(sum)
        return sum
     
multiple_num(5,5)

## and
def mul_num(a=3, b=4):
      print(a*b)
      return a*b

mul_num()

## waf to print the lenght of a list.(list is the parameter)
cities = ["delhi","noida","jaipur","jodhpur","gurgaon"]
heroes = ["salman khan","varun dhavan","ranveer kapoor","sharuk khan"]

def print_len(list):
      print(len(list))

print_len(cities)
print_len(heroes)
     

## waf to find the factorial of n.(n is the parameter)

def cal_fact(n):
      fact = 1
      for i in range(1,n+1):
           fact *= i
      print(fact)

cal_fact(5)
cal_fact(6)


## waf to convert USD to INR
def converter(usd_val):
      inr_val = usd_val * 83
      print(usd_val, "USD =", inr_val, "INR")

converter(1)
converter(5)

## my code
num = int(input("enter the number :"))
def testing(num):
      if (num%2 == 0):
           print("even")
      else:
           print("odd")
testing(num)



# recursion  >> when a function calls itself repeatedly

def show(n):
      if (n == 0):  # यदि n 0 है
           return    # फ़ंक्शन को समाप्त कर दो
      print(n)       # n को प्रिंट करो
      show(n-1)      # `show` को n-1 के साथ फिर से कॉल करो

show(6)  # इस फ़ंक्शन को 6 से शुरू करके कॉल करें


# return n!
def fact(n):
      if( n==0 or n == 1):
           return 1
      return fact(n-1) *n

print(fact(6))


## write a recursive function to calculate the sum of first n natural numbers
def cal_sum(n):
      if(n == 0):
           return 0
      return cal_sum(n-1) + n

sum = cal_sum(5)
print(sum)
     

## write a recursive function to print all element in a list
##hint.use list & index as parameters.

def print_list(lst, index):
     if index == len(lst):  # Stop recursion when index reaches the length of the list
         return
     print(lst[index])      # Print the current item in the list
     print_list(lst, index + 1)  # Recursive call to print the next item

# # Initialize the list
fruits = ["banana", "mango", "apple", "grapes"]
print_list(fruits, 0)  # Start from index 0













