print('\n****************************** END ******************************\n')

# https://www.w3schools.com/python/python_variables.asp



# type of a variable
x = 'amit'
y = 54
print(type(x), type(y))
print('\n****************************** END ******************************\n')


# print function
# print without \n at end
print("Hello World ", end="")
print(" New line")
print('\n****************************** END ******************************\n')


# multiple assignments are a thing in python
x, y, z = 'amit', 'is a', 'good boy'
print(x, z)
# one value to multiple variables
x = y = z = 0
print(x, y, z)
# unpacking collection
x, y, z = ["apple", "banana", "cherry"]
print(x, y, z)
print('\n****************************** END ******************************\n')


# https://www.geeksforgeeks.org/python-output-formatting/
# print integer and float value
print("Geeks : %5d, Portal : %5.2f" % (1, 05.333))
# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
# using format() method and referring a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
print('{1} and {0}'.format('Geeks', 'Portal'))
# python > v3.6
x = 'Geeks' 
y = 'Treats'
print(f'I love {x} for {y}')
# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'.format('Geeks', 'For', other ='Geeks'))
# using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 00.546))
# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))
print('\n****************************** END ******************************\n')


# global function
# variables outside of any function are global
# to make a variable inside function global use the 'global keyword'
def myfunc():
    global x
    x = "fantastic"
myfunc()
print(x)
# this can also be used to change the value of global variable from inside the function
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) 
print('\n****************************** END ******************************\n')



# python data types
x = "Hello World"
print(x, type(x))
x = 20
print(x, type(x))
x = 20.5
print(x, type(x))
x = 3 + 1j
print(x, type(x))
x = ["apple", "banana", "cherry"]
print(x, type(x))
x = ("apple", "banana", "cherry")
print(x, type(x))
x = range(6)
print(x, type(x))
x = {"name" : "John", "age" : 36}
print(x, type(x))
x = {"apple", "banana", "cherry"}
print(x, type(x))
x = frozenset({"apple", "banana", "cherry"})
print(x, type(x))
x = True
print(x, type(x))
x = b"Hello"
print(x, type(x))
x = bytearray(5)
print(x, type(x))
x = memoryview(bytes(5))
print(x, type(x))
x = None
print(x, type(x))
print('\n****************************** END ******************************\n')



# random numbers in python
# https://www.w3schools.com/python/module_random.asp
import random
print(random.random())
print(random.randrange(1, 100))
print('\n****************************** END ******************************\n')



# strings in python
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_strings_methods.asp
# multiline string
x = '''my name
is amit 
kumar'''
print(x)
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1.
print(x[0])
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)
txt = 'amit kumar'
print('mit k' in txt)
# upper case
print(txt.upper())
# lower case
print(txt.lower())
# remove whitespaces from beginning and end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 
# replace substring with another string
a = "Hello, World! Hero Honda"
print(a.replace("He", "J"))
print('\n****************************** END ******************************\n')



# operators in python
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators
# Identity operators: Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
a = 'amit kumar'
b = 'amit kumar'
c = 'priya jha'
print(a is b)
print(b is c)
a = [1, 2]
b = [1, 2]
c = [2, 1, 3]
print(a is b)
print(b is c)
# Membership operators
print(1 in a)
print(1 not in a)
# Bitwise operators
print(1 & 1) 
print(1 & 2) # 1 = 01, 2 = 10
print(7 | 7) 
print(8 | 7) # 8 = 1000, 7 = 0111, 8 | 7 = 1111
print(9 ^ 7) # XOR, 9 = 1001, 7 = 0111, 9 XOR 7 = 1110
print(~8) # 7 = 1000, NOT 8 = 0111(2's complement)
print(2 << 3) # 2 = 10, 2 << 3 = 10000, multiply by 2^3
print(4 >> 2) # 4 = 100, 2 >> 2 = 001
print('\n****************************** END ******************************\n')
