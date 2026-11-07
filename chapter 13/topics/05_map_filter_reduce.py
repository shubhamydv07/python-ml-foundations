# map() function in Python is a built-in utility that applies a 
# specific function to every item in an iterable 
# (like a list, tuple, or dictionary) and 
# returns a lazy iterator (a map object) 
# containing the transformed results

# Instead of writing a traditional for loop to modify every element
#  in a collection, map() allows you to perform element-wise 
# transformations with cleaner, more concise code

# Syntax = map(function, input_list)

from functools import reduce

l = [12,13,18,79,76]
square = lambda x:x*x

sqlist = map(square,l)
print(tuple(sqlist)) 
#Map will give iterable output , to dispaly that result we need to
# convert that into list,tuple etc




# FILTER -It creates list of items for which function returns true
#Syntax - list(filter(function))

def myFunct(n):
    if (n%2 ==0):
        return True
    return False

onlyEven = filter(myFunct , l)
print(list(onlyEven))




# REDUCE FUNCTION - It runs sequentially pair of elements
# We need to import it from functools using - "from functools import reduce"
#Syntax - "val = reduce (function, list1)""

def sum (a,b):
    return a + b

mult = lambda x,y:x*y

print(reduce(sum , l))
print(reduce(mult,l))
