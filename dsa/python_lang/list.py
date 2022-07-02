


list1 = ['amit', 'priya', 'tom', 'jerry', 77]

# length of list
a = len(list1)
print(a)
print('\n****************************** END ******************************\n')



# tupe of list
b = type(list1)
print(b)
print('\n****************************** END ******************************\n')



# list contructor
list2 = list(('amit', 'priya', 'tom', 'jerry', 77))
print(len(list2))
print(type(list2))
print('\n****************************** END ******************************\n')



# indexing
print(list1[0]) # first element
print(list1[1]) # second element
print(list1[-1]) # last element
print(list1[-2]) # second last element
print(list1[0:2]) # 0-2th element, 2th not included
print('\n****************************** END ******************************\n')



# check if item exists in list
if 'amit' in list1:
    print('Yes')
if 'sapan' not in list1:
    print('yes')
print('\n****************************** END ******************************\n')



# changing list item
list1[0] = "amit the best"
print(list1)
# change range of items
list1[0:2] = ["amit the best", "priya the best"]
print(list1)
# change multiple elements with a single value
list2[0:2] = ["kids"]
print(list2)
print('\n****************************** END ******************************\n')



# insert element at specific index
print(list1)
list1.insert(0, "papaya")
print(list1)
# add item to the end
list1.append("added to end")
print(list1)
# add element from another list to current list
list3 = ['one', 'two', 'three']
list1.extend(list3) # you can add any iterable object (tuples, sets, dictionaries etc.)
print(list1)
print('\n****************************** END ******************************\n')



# remove specific list item, we know its value
list1.remove('papaya')
print(list1)
# remove item at specific index
list1.pop(5) # If you do not specify the index, the pop() method removes the last item.
print(list1)
# another way to remove element at a specific index
list1.insert(5, "im the best")
print(list1)
del list1[5]
print(list1)
# delete list completely, deletes the variable too
# del list3
# empty the list
print(list2)
list2.clear()
print(list2)
print('\n****************************** END ******************************\n')




# list comprehension
# find fruits with 'a' in their name
fruits = ["cherry", "kiwi", "apple", "banana", "mango"]
# approach 1
new_fruits = []
for x in fruits:
    if 'a' in x:
        new_fruits.append(x)
print(new_fruits)
# method 2
new_fruits.clear()
new_fruits = [x for x in fruits if 'a' in x]
print(new_fruits)
print('\n****************************** END ******************************\n')




# sorting
print(fruits)
fruits.sort()
print(fruits)
list3 = [100, 50, 65, 82, 23]
print(list3)
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)
print('\n****************************** END ******************************\n')



# customised sort
# https://developers.google.com/edu/python/sorting#custom-sorting-with-key=
print(fruits)
def myFunc(x): # The key function takes in 1 value and returns 1 value
    return x[1]
# sort fruits name by second character
fruits.sort(key=myFunc)
print(fruits)
# more examples
fruits.sort(key=len)
print(fruits)
# another way
x = sorted(fruits, key=myFunc) # sorted doesnt change the original list, and words exactly same as .sort()
print(x)
# reversing a list
print(list3)
list3.reverse()
print(list3)
print('\n****************************** END ******************************\n')



# copying lists
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
list4 = list3
list4[0] = "Anaconda"
list3[0] = "Snake"
print(list3, list4)
list4 = list3.copy()
list4 = list(list3) # same as above
print(list4)
list4[0] = "Anaconda"
list3[0] = "Snake"
print(list3, list4)
print('\n****************************** END ******************************\n')



# concatenate/join list
list1.clear()
list2.clear()
list3.clear()
list4.clear()
fruits.clear()
new_fruits.clear()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# using the extend method
list3.clear()
print(list3)
list1.extend(list2)
print(list1)
print('\n****************************** END ******************************\n')


# count the elements with the specified value
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)
print('\n****************************** END ******************************\n')







