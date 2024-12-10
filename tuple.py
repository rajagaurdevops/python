# tuple
# creating tuple
tuple = (1,2,2.5,"hello")
print(tuple)


# tuple connot change but re-assign
a = (1,2,3,4)
print(a)

a = (5,6,7,8)
print(a)


# deleting tuple
tuple = (2,4,6,8)
# del tuple[0]      # TypeError: 'tuple' object doesn't support item deletion
del tuple
print(tuple)


# check leanth of tuple's item
tuple = (2,4,6,8,10)
print(len(tuple))


# iterating tuple items using for loop
tuple = (1,2,3,"hello")
for i in tuple:
    print(i)

# wap to count the numbers of student with "A" grade in the following tupe
grade = ("c","d","a","a","b","b","a")
print(grade.count("a"))


# store the above values in a list & sort them from "a" to "d"
list = ["c","d","a","a","b","b","a"]
list.sort()
print (list)    