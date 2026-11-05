friends = ["Apple" , 'Orange' , 5 , 345.07 , "shubham" , "rohit" , False]
print(friends)

# IF WE APPLY ANY METHOD ON LISTS THEN NEW LIST WHICH WILL COME AFTER , THAT WILL BE CHANGE
# THE ORIGINAL LIST WILL BE REPLACE BY NEW ONE 


friends.append("NIT KURUKSHETRA") # APPEND NEW STRING AFTER LAST STRING

print(friends[7])

l1 = [1 ,34 , 78 , 20 , 18]


l1.sort() #ARRANGE ALPHABETS IN ASCENDING ORDER
print(l1)


l1.reverse() #REVERSE THE LIST
print(l1)


friends.insert(3,"coder") #THIS WILL ADD "CODER" AT THE INDEX 3
print(friends)


l1.pop(3)         #THIS WILL REMOVE ELEMENT WHICH IS STORED AT INDEX 3    
friends.pop(6)    #THIS WILL REMOVE ELEMENT WHICH IS STORED AT INDEX 6
print(l1)
print(friends)

friends.remove('Apple')  #IT WILL REMOVE 'Apple' FOOM THE LIST
print(friends)

print(type(friends[3]))

