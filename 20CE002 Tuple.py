# StudentID:    20CE002
# Student Name: Nidhi Batra

# a.Write a Python Program to Create a tuple with different datatype.
A = ("nidhi", 15.256, 12)
print(A)

# b. write a Python Program to create tuple with numbers and print one item.
B = ('a', 1, 'b', 2, 'c', 3, 'd', 4)
item = B[2]
print(item)

# c. write a Python Program to add an item in a tuple.
C = (2, 4, 6, 8, 10, 12)
print(C)
C = C + (14,)
print(C)

C = C[:3] + (11, 13, 15)
print(C)

listx = list(C)
listx.append(18)
D = tuple(listx)
print(D)

# d. Write a Python Program to convert tuple to a String.
E = ('N', 'I', 'D', 'H', 'I')
string =  ''.join(E)
print(string)

# e. write a python Program to find the length of tuple.
print(len(E))    # length of upper tuple