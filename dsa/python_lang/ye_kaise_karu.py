# https://www.w3schools.com/python/default.asp



# convert string to list of chars
myStr = ' Amit Kumar ';
myStr = list(myStr) # with spaces
print(myStr)
op1 = list(filter(' '.__ne__, myStr)) # remove spaces method 1, can replace ' ' with anything to remove all its occurence
print(op1) # without spaces
op2 = [i for i in myStr if i != " "] # remove spaces method 2, can replace ' ' with anything to remove all its occurence
print(op2)
print('\n****************************** END ******************************\n')



# removing duplicated from a list
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist) 
print('\n****************************** END ******************************\n')



# reversing a string
myStr = 'Hello World'
revStr = myStr [::-1]
print(myStr)
print(revStr)
print('\n****************************** END ******************************\n')



# multiline comment in python is a mython
# Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:
"""
This is a comment
written in
more than just one line, actually its a string not assigned to 
any variable so it will be ignored by interpreter, but can work as comment, wtf!
"""
print('Hello World')
print('\n****************************** END ******************************\n')



# random numbers in python
# https://www.w3schools.com/python/module_random.asp
import random
print(random.random())
print(random.randrange(1, 100))
print('\n****************************** END ******************************\n')



# check if a list contains all unique elements
def all_unique(lst):
  return len(lst) == len(set(lst))
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
print(all_unique(x))  # True
print(all_unique(y))  # False
print('\n****************************** END ******************************\n')




# transpose a matrix, hard way
mat = [[1,1,1], [1,2,3], [4,5,6]]
new_mat = []
for i in range(len(mat)):
  temp = []
  for j in range(len(mat[i])):
    temp.append(mat[j][i])
    new_mat.append(temp)
print(mat)
print(new_mat)
print('\n****************************** END ******************************\n')


