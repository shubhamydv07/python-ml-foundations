from functools import reduce
numbers = [12 , 45,56,78,30,15,10,24,68]

def greater(a,b):
    if a>b:
        return a
    return b

max_value = reduce(greater , numbers)

print(max_value)

# ALternative method
max_value = lambda x,y:x if x>y else y 
print(reduce(max_value , numbers))
