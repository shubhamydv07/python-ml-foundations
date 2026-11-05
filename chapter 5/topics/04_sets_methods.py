s = {1 , 56 , 6 , 7 , 6 , 8 , 123 , "shubham"}

print(s , type(s))

s.add(18)   # SETS ARE MUTABLE
s.add(17)   # it add elements on set
s.remove(56) # IT REMOVE ELEMENT ON SETS
print(s)


print(len(s))       # Returns the length of the set

s.remove(1)         # Removes the specified element
print(s)

s.pop()             # Removes an arbitrary element
print(s)

s.clear()           # Empties the set
print(s)

# SET OPERATIONS 
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))      # Returns a new set with all items from both sets
print(set1.intersection(set2)) # Returns a new set with only common items


# Set itself = mutable
# Elements inside = must be immutable
s = {1, 2, (3, 4)}   #  tuple allowed
s = {1, 2, [3, 4]}   #  error (list is mutable)


# CANNOT ACCESS ELEMENT BY INDEX
s = {1, 2, 3}
print(s[0])   #  error


# FROZEN SET EXIST AND IT IS IMMUTABLE
fs = frozenset([1, 2, 3])
fs.add(4)   #  error