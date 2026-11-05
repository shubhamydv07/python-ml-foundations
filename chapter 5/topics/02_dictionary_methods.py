marks = {
    "shubham" : 78 ,
    "rahul" : 67 , 
    "rohan" : 89 ,
    0 : "amrinder" ,
}

print(marks.items())     # Returns a list of (key,value) tuples


print(marks.keys())      # Returns a list of keys


print(marks.values())    # Returns a list of values


marks.update({"shubham" : 90 , "renuka" : 99})   # UPDATES THE DICTIONARY WITH KEY - VALUE PAIR 
print(marks)                                     # BECAUSE DICTIONARY IS MUTTABLE


print(marks.get("shubham"))    # Returns the value of the specified keys


# print(marks.get("shubham2"))  # IT WIL PRINT 'NONE'
# print(marks["shubham2"])      # IT WILL GIVE ERROR 


d = {"a": 1, "b": 2}
d.pop("a")    # REMOVES A KEY FROM THE DICTIONARY
print(d)   


f = {"a": 1, "b": 2}
f.popitem()    # REMOVES LAST INSERTED ITEM
print(f)


g = {"a": 1, "b": 2}
g.clear()    # CLEARS THE DICTIONARY
print(g)


h = {"a": 1, "b": 2}
del h["a"]
print(h)    # DELETES THE DICTIONARY SPECIFIC ITEM