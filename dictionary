# dictionary

 # creating dictionary
dict = {
     "name": "raja",
     "age": 18,
     "marks": 85,
      12 : 24,
 }
 print(dict)
 print(dict["name"])
 print(dict["age"])
 print(dict["marks"])
 print(dict[12])
 print(type(dict))

# change dictionary value
 dict["name"] = "nishant"
 dict["age"] = 19
 dict["marks"] = 95
 print(dict)

# creating empty dict
 null_dict = {}
 print(null_dict)

# nested dictionary
student = {
    "name" : "rahul kumar",
    "subject" : {
        "python":5,
        "clanguage":5,
        "data structure": 8

    }
}
 print(student["subject"]["python"])
 print(student["subject"]["clanguage"])

# dictionary method
# mydict.keys() # return all keys

 print(tuple(student.keys()))  # tuple to form in the keys
 print(len(tuple(student.keys())))

 print(len(student))

# mydict.values()   # return all values
 print(student.values())

# mydict.items()
 print(list(student.items()))
 pairs =list(student.items())
 print(pairs[0])

# mydict.get("key") # return the key according to value
 print(student["name"])  # if invalde to return error
 print(student.get("name"))  # no error only none

# mydict.update(new dict)   # inserts the specified items to the dictionary
student.update({"city":"bari" ,"name":"raja kumar"})
print(student)

# change dictionary keys

dict = {"name":"raja","name1":"nishant","name2":"bhola","name3":"aman"}
 dict["name5"]=dict.pop("name")
 print(dict)

# add dictionary element
 dict ["name5"]="sachin"

# delete dictionary element
del dict["name3"]
print(dict)

# store following word meanings in a python dictionary
 dict = {
     "cat":"a small animal",
     "tabel":["a piece of furniture","list of facts & figures"]
 }
 print(dict)

'''
 you are given a list of subject for students.
 Assume one classroom is required for 1 subject
 how many classrooms are needed by all student
'''
'''
"python","java","python","c++","javascript","java","python","java","c++","c"
'''
subject = {
     "python", "java", "c++", "python", "javascript", "java",
     "python", "java", "c++", "c"
 }
print(len(subject))



'''
wap to enter of 3 subject from the user and store them in a dictionary.
start with an empty dict & add one by one .
subject name as key & marks as value
'''
marks = {}

x = int(input("Enter Python marks: "))
marks.update({"python": x})

y = int(input("Enter C language marks: "))
marks.update({"clanguage": y})

z = int(input("Enter Algorithm marks: "))
marks.update({"algorithm": z})

print(marks)