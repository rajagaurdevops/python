# oop  >> object oriented programming system
# definition  >> to map with real world scenarios, we started using object in code


        # class & Object in python >> class is a blueprint for creating object.

   # creating class

class student: 
   name = "raja kumar"


  # creating object (instance)
s1 = student()
print(s1.name) 
     


class car:
   color = "black"
   brand = "thar"

car1 = car()
print(car1.color)
print(car1.brand)


# __init__Function
# Constructor  >> All classses have a function called _init_();

class student:
   collage_name = "Gpc collage"
   name = "anonymous"    # class attributes
   # parameterized constructors
   def __init__(self, fullname, marks):
      self.name = fullname   # obj attr > class attr
      self.marks = marks
      print("adding new student in database")

s1 = student("Raja", 85)  
print(s1.name,s1.marks)

print(s1.name)


  # methods >> methods are function that belong to objects.
class student:
   collage_name = "Gpc collage"
   def __init__(self,name,marks):
       self.name = name      # constructor
       self.marks = marks

   def welcome(self):
      print("welcome student",self.name)

   def get_marks(self):   # methods
      return self.marks

s1 = student("raja", 98)
s1.welcome()
print(s1.get_marks())


'''
create student class that takes name  marks of 3 subjects as arguments 
in constructor.then create a method to print the average.

'''
class student:
   def __init__(self,name,marks):
      self.name = name
      self.marks = marks

   def get_avg(self):
      sum = 0
      for i in self.marks:
         sum += i
      print("hii", self.name, "your avg score is:", sum/3)


s1 = student("rajakumar", [98,78,79])
s1.get_avg()

s1.name = "nishant"
s1.get_avg()

# static method >> methods that dont use the self parameter(work at class level)
class student:
   @staticmethod
   def collage():     # decorator
      print("GPC COLLAGE")

   collage()



    # Abstraction
'''
Hinding the implementation details of a class and only
showing the essential features to the user

'''
class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.cluth = False

  def start(self):
    self.cluth = True
    self.acc = True
    print("car started..")
car1 = Car()
car1.start()
      

# Encapusulation >> wrapping dat and function infi a singal unit(object)

      ## let's practices question
'''
create Account class with 2 attributes-blance & account no.
create methods for debit, credit & printing the balnce

'''
class Account:
  def __init__(self, bal, acc):
    self.balance = bal
    self.account_no = acc

  #debit method
  def debit(self, amount):
     self.balance -= amount
     print("Rs", amount, "was debited")
     print("total balance =", self.get_balance())


  def credit(self, amount):
     self.balance += amount
     print("Rs", amount, "was credited")
     print("total balance =", self.get_balance())


  def get_balance(self):
    return self.balance


acc1 = Account(10000, 145510801644)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)



https://www.boardinfinity.com/blog/content/images/2023/03/Copy-of-Copy-of-Copy-of-Untitled-Design-1-1.png