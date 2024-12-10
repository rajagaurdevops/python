# file I/o in python >> python can be used to perform operation on a file(read,write data)

## type of file
f = open("filename","mode")

f = open("Demo.txt", "r")  # read mode
data = f.read(4) 
print(data)
print(type(data))
f.close()

## Reading a file

f = open("demo.txt","r") 
data = f.read()   # reads entire file
data = f.readline(3)  # reads one line at a time


f  = open("Demo.txt","r")

line2 = f.readline()   # read one line at a time
print(line2)

line3 = f.readline()  # read one line at a time
print(line3)

line4 = f.readline()  # read one line at a time
print(line4)

f.close()


## Writing to a file

f = open("Demo.txt","w")   # (w)overwrite the entire file

f.write("this is new line")

f.close()

f = open("Demo.txt","a")   #(a)adds to the file

f.write("\nthis is next line")

f.close()


## creating file 
f = open("raja.txt","w")   ## creating raja.txt file
f.close()

f = open("raja.txt","r+")   ## open for reading and writing. the stream is positioned at the beginning of the file
f.write("abc")    ## now raja.txt >> abcs is a simple file
print(f.read())
f.close()

f = open("raja.txt","w+")   ## the file is created if it does not exit, otherwise it is truncated
print(f.read())
f.write("abc")
f.close()


## with syntax
  ## with open ("file_name","mode") as f:
        ## data = f.read()

with open("raja.txt","r") as f:
     data = f.read()
     print(data)

with open("raja.txt","w") as f:   ## stored new data in raja.txt file
     f.write("new data")


## deleting a file  >> (using the os module)
## module (like a code library) is a file written by another programmer that generally has a function we can use

import os

os.remove("testing")  ## remove testing file


##q.1 create a new file "practice.txt" using python.add the following data in it
with  open("practice.txt","w") as f:
     f.write("hi everyone\nwe are learning file I/o\n")
     f.write("using java.\nI like programming in java")


##q.2  waf that replaces all occurrences of "java" with "python" in above file
with open("practice.txt","r") as f:
     data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
     f.write(new_data)
 

##q.3  search if the word "learning" exists in the file or not.
def  chaking_word():
         word = "learning"
         with open("practice.txt","r") as f:
             data = f.read()
         if(data.find(word) != -1):
             print("found")
         else:
             print("not found")
chaking_word()


## waf to find in which of the file does the word "learning" occur first,
## print -1 if word not found
def check_for_line():
     word = "programming"
     data = True
     line_no = 1
     with open("practice.txt","r") as f:
         while data:
             data = f.readline()
             if (word in data):
                 print(line_no)
                 return
             line_no +=1

     return -1

print(check_for_line())


## from a file containing numbers separated by comma,print the count of even numbers

count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
         if(data[i] == ","):
             print(num)
             num = ""
         else:
             num += data[i]
       ## second method solve this question

    num = data.split(",")
    for x in num:
        if(int(x)%2 == 0):

            count +=1

print(count)
    
